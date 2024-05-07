"""
Scans Manticore Search manual files and compile into a single big file.
"""

from functools import cache
import re
from collections.abc import Iterator
from pathlib import Path
from shutil import copy, rmtree
from rich import print

import markdown
import msgspec
from jinja2 import Template

MANTICORE_VERSION = "6.2.12 (Aug 23, 2023)"

SRC_ROOT: Path = Path("sources/")
DST_ROOT = Path("docs/")
ASSETS_ROOT = Path("assets/")

# Lines looks like this:
# "* [1️⃣ Installation](Installation/Installation.md)
LINE_PATTERN = r"^(\s*)\* \[(.+)\](.+)?$"

# Double anchor pattern
DOUBLE_ANCHOR_PATTERN = r"\([^\)#]+#([^\)#]+)#([^\)#]+)\)"

MD_BULET = r"^(\s*)\*"

# Store destination paths for each source path, used to fix links.
DESTINATION_FOR_PATH: dict[str, str] = {}

WARNINGS : list[str] = []

class Entry(msgspec.Struct, omit_defaults=True):
    title: str
    path: str | None = None
    anchor: str | None = None
    children: list["Entry"] = []

    toc_path: str = ""
    breadcrumb: str = ""
    nest_level: int = 0

    def cssid(self) -> str:
        return f"toc-{self.breadcrumb}-{self.title.replace(' ', '_').lower()}"

    def clean_breadcrumb(self) -> str:
        parts = self.breadcrumb.split(".")
        cleaned_parts = [part.lstrip("0") for part in parts]
        return ".".join(cleaned_parts)

    def filename(self) -> str:
        """Name of a file for this entry, to be placed in a chapter path."""
        return f"{self.breadcrumb}-{self.title.replace(" ", "_").lower()}.html"

    def print(self, indent: str = ""):
        print(f"{indent}{self.breadcrumb or " "} {self.title} [{self.path}]")
        for entry in self.children:
            entry.print(indent + "  ")

    def dfs(self) -> Iterator["Entry"]:
        yield self
        for child in self.children:
            yield from child.dfs()

    def collect_paths(self) -> set[Path]:
        paths: set[Path] = set()
        for entry in root.dfs():
            if entry.path:
                paths.add(SRC_ROOT / entry.path)
        return paths

    def source_path(self) -> Path | None:
        if not self.path:
            return None
        return SRC_ROOT / self.path

    def source_exists(self) -> bool:
        p = self.source_path()
        return (p or False) and p.exists() and p.is_file()

    def __hash__(self):
        """Since we are only using this to cache to_html, we can use the path as a hash."""
        return hash(self.path)

    @cache
    def html_header_and_content(self):
        """Returns a tuple with the header and the content of the HTML file."""
        html = self.to_html()
        parts = html.split("</h1>", maxsplit=1)

        if len(parts) == 1:
            return "", html
        else:
            return (parts[0] + "</h1>"), parts[1]

    @cache
    def to_html(self) -> str:
        if not self.source_exists():
            return ""

        p: Path = self.source_path()  # type: ignore

        buffer: list[str] = list()

        def open_div(klass: str):
            buffer.append(f"\n<div class='{klass}'>\n")

        def close_div(klass: str):
            buffer.append("\n</div>\n")

        # We'll read file line by line to do a lil cleanup.
        with p.open("r", encoding="utf-8") as file:
            source = file.read()

            # Fix links. We'll need to fix double anchors when scannign line by line.
            source = source.replace("../../", "")
            for source_path, dest_path in DESTINATION_FOR_PATH.items():
                source = source.replace(source_path, dest_path)

            # PyMarkdown removes the () from the links, so we need to fix them too.
            source = source.replace("%28%29", "")

            last_line = ""

            num_intros = 0
            num_requests = 0
            example_name = ""
            in_code_block = False
            insert_code_block = False

            for line in source.splitlines(keepends=True):
                # PyMarkdown doesn't like lists that are not separated by empty lines.
                md_match = re.match(MD_BULET, line)
                if md_match:
                    # PyMarkdown doesn't like nested items that are not nested in multiples of 4.
                    spaces = " " * 4 * (max(len(md_match[1]) - 2, 0) // 2)
                    line = f"{spaces}{line.lstrip()}"

                    if not re.match(MD_BULET, last_line):
                        buffer.append("\n")

                # Previously when we replaced links we may have produced double anchors, so fix them.
                matches = re.findall(DOUBLE_ANCHOR_PATTERN, line, re.UNICODE)
                if matches:
                    for match in matches:
                        line = line.replace(
                            f"#{match[0]}#{match[1]}", f"#{match[1].lower()}"
                        )

                if in_code_block and line.find("#####") >= 0:
                    open_div("item-select")
                    buffer.append(f"{line.replace('#', '').replace(':', '').strip()}")
                    close_div("item-select")
                else:
                    buffer.append(line)

                last_line = line

                # Let's add some markup for the code blocks.
                if line.startswith("<!-- example"):
                    in_code_block = True
                    insert_code_block = True
                    num_intros = 0
                    num_requests = 0
                    example_name = line.strip()
                elif line.startswith("<!-- request"):
                    num_requests += 1
                elif line.startswith("<!-- intro"):
                    num_intros += 1
                    if in_code_block:
                        if insert_code_block:
                            open_div("xcodeblock")
                            open_div("xcodeblock-item")
                            insert_code_block = False
                        else:
                            close_div("xcodeblock-item")
                            open_div("xcodeblock-item")
                elif line.startswith("<!-- end"):
                    if num_intros != num_requests:
                        WARNINGS.append(f"{self.path}: {example_name} has {num_intros} intros and {num_requests} requests")
                    if in_code_block:
                        close_div("xcodeblock-item")
                        close_div("xcodeblock")
                    in_code_block = False

        # if self.path:
        #     with open(f"fix-{self.path.replace('/', '_')}", "w") as f:
        #         f.write("".join(buffer))

        return markdown.markdown(
            "".join(buffer),
            extensions=[
                "extra",
                "toc",
                "fenced_code",
                "codehilite",
                "tables",
                "nl2br",
            ],
        )


def parse_entries() -> Entry:
    root = Entry(title="Manticore Search Manual")

    stack = [root]

    with open(SRC_ROOT / "README.md", "r") as file:
        lines = file.readlines()
        for line in lines:
            matches = re.findall(LINE_PATTERN, line, re.UNICODE)

            indent, title, href = matches[0]
            href = href.strip()[1:-1]
            indent = 1 + len(indent) // 4  # Indents will go from 1 to 4.

            title = re.sub(r"[^A-Za-z0-9 _\-]+", "", title).strip()
            title = re.sub(r"^\d+\s*", r"", title).strip()

            entry = Entry(title=title)

            if "#" in href:
                path, anchor = href.split("#")  # type: ignore
                entry.path = path
                entry.anchor = anchor
            else:
                entry.path = href

            if not entry.path:
                entry.path = None

            parent: Entry

            if indent == len(stack):
                parent = stack[-1]
                parent.children.append(entry)

            elif indent > len(stack):
                parent = stack[-1].children[-1]
                parent.children.append(entry)
                stack.append(parent)
            else:
                while len(stack) > indent:
                    stack.pop()
                parent = stack[-1]
                parent.children.append(entry)

            entry.nest_level = indent
            if parent.breadcrumb:
                entry.breadcrumb = f"{parent.breadcrumb}.{len(parent.children):02}"
            else:
                entry.breadcrumb = f"{len(parent.children):02}"

    return root


def sanity_checks(root: Entry):
    errors: list[str] = []

    # Sanity check: Paths from ToC should exist.
    toc_paths = root.collect_paths()
    for path in toc_paths:
        if not path.exists():
            errors.append(f"{path} is referenced in ToC but does NOT exist!")

    existing_sources: set[Path] = set()
    for path in SRC_ROOT.rglob("*.md"):
        existing_sources.add(Path(path))

    # Sanity check: no missing documents.
    missing_documents = toc_paths - existing_sources
    if len(missing_documents) > 0:
        errors.append(f"ToC is missing documents!: ${missing_documents}")

    # Sanity check: we are only skipping README.md
    skipped = existing_sources - toc_paths
    skipped.remove(SRC_ROOT / "README.md")
    for skip in skipped:
        errors.append(f"ToC skips existing file!: {skip}")

    if errors:
        print("errors found!")
        for error in errors:
            print(error)
        exit(1)


def write_output(root: Entry):
    """Generate the output file."""

    if DST_ROOT.exists():
        rmtree(DST_ROOT)

    DST_ROOT.mkdir(parents=True, exist_ok=True)

    # Copy assets.
    copy(ASSETS_ROOT / "common.css", DST_ROOT)
    copy(ASSETS_ROOT / "toc.css", DST_ROOT)
    copy(ASSETS_ROOT / "chapter.css", DST_ROOT)
    copy(ASSETS_ROOT / "pygments.css", DST_ROOT)

    img_ext: set[str] = set([".png", ".jpg", ".jpeg", ".gif", ".svg"])
    for path in SRC_ROOT.rglob("*"):
        if path.suffix in img_ext:
            copy(path, DST_ROOT)

    # Prepare the ToC.
    toc_entries: list[Entry] = []
    first_path: Path | None = None

    print("* Scanning ToC...")
    for top_entry in root.children:
        chapter_path = DST_ROOT / top_entry.filename()
        rel_path = chapter_path.relative_to(DST_ROOT)

        if not first_path:
            first_path = rel_path

        for chapter_item in top_entry.dfs():
            chapter_item.toc_path = f"{rel_path}#{chapter_item.cssid()}"
            toc_entries.append(chapter_item)

            source_path = chapter_item.source_path()
            if source_path:
                DESTINATION_FOR_PATH[source_path.relative_to(SRC_ROOT).as_posix()] = (
                    chapter_item.toc_path
                )

    toc = DST_ROOT / "index.html"
    print(f"* Writing {toc}...")
    with toc.open("w") as dst:
        template = Template(open(ASSETS_ROOT / "toc.html.j2").read())
        result = template.render(
            entries=toc_entries,
            version=MANTICORE_VERSION,
            first_path=first_path,
        )
        dst.write(result)

    chapter_template = Template(open(ASSETS_ROOT / "chapter.html.j2", "r").read())

    for top_entry in root.children:
        chap = DST_ROOT / top_entry.filename()
        print(f"* Writing {chap}...")
        with chap.open("w") as dst:
            result = chapter_template.render(
                entries=[chapter for chapter in top_entry.dfs()],
                version=MANTICORE_VERSION,
                chapter_title=top_entry.title,
            )
            dst.write(result)


root = parse_entries()
sanity_checks(root)
write_output(root)

print("\nDone!\n")

if WARNINGS:
    for warning in WARNINGS:
        print(warning)
    print(f"{len(WARNINGS)} warnings.")
