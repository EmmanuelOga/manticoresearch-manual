* [☝ Introduction](Introduction.md)
* [❗ Read this first](Read_this_first.md)
* [1️⃣ Installation](Installation/Installation.md)
    * [• Docker](Installation/Docker.md)
    * [• RedHat and Centos](Installation/RHEL_and_Centos.md)
    * [• Debian and Ubuntu](Installation/Debian_and_Ubuntu.md)
    * [• MacOS](Installation/MacOS.md)
    * [• Windows](Installation/Windows.md)
    * [• Compiling from sources](Installation/Compiling_from_sources.md)
    * [• Migration from Sphinx](Installation/Migration_from_Sphinx.md)
* [🔰 Quick start guide](Quick_start_guide.md)
* [2️⃣ Starting the server](Starting_the_server.md)
    * [• In Linux](Starting_the_server/Linux.md)
    * [• Manually](Starting_the_server/Manually.md)
    * [• In Docker](Starting_the_server/Docker.md)
    * [• In Windows](Starting_the_server/Windows.md)
    * [• In MacOS](Starting_the_server/MacOS.md)
* [3️⃣ Creating a table](Creating_a_table.md)
    * [• Data types](Creating_a_table/Data_types.md)
        * [• Row-wise and columnar attribute storages](Creating_a_table/Data_types.md#Row-wise-and-columnar-attribute-storages)
    * [Creating a local table](Creating_a_table/Local_tables.md)
        * [✔ Real-time table](Creating_a_table/Local_tables/Real-time_table.md)
        * [• Plain table](Creating_a_table/Local_tables/Plain_table.md)
        * [• Plain and real-time table settings](Creating_a_table/Local_tables/Plain_and_real-time_table_settings.md)
        * [• Percolate table](Creating_a_table/Local_tables/Percolate_table.md)
        * [• Template table](Creating_a_table/Local_tables/Template_table.md)
    * [⪢ NLP and tokenization]
        * [• Data tokenization](Creating_a_table/NLP_and_tokenization/Data_tokenization.md)
        * [• Supported languages](Creating_a_table/NLP_and_tokenization/Supported_languages.md)
        * [• CJK](Creating_a_table/NLP_and_tokenization/CJK.md)
        * [• Low-level tokenization](Creating_a_table/NLP_and_tokenization/Low-level_tokenization.md)
        * [• Wildcard searching settings](Creating_a_table/NLP_and_tokenization/Wildcard_searching_settings.md)
        * [• Ignoring stop words](Creating_a_table/NLP_and_tokenization/Ignoring_stop-words.md)
        * [• Word forms](Creating_a_table/NLP_and_tokenization/Wordforms.md)
        * [• Exceptions](Creating_a_table/NLP_and_tokenization/Exceptions.md)
        * [• Morphology](Creating_a_table/NLP_and_tokenization/Morphology.md)
        * [• Advanced HTML tokenization](Creating_a_table/NLP_and_tokenization/Advanced_HTML_tokenization.md)
    * [⪢ Creating a distributed table](Creating_a_table/Creating_a_distributed_table/Creating_a_distributed_table.md)
        * [• Creating a local distributed table](Creating_a_table/Creating_a_distributed_table/Creating_a_local_distributed_table.md)
        * [• Remote tables](Creating_a_table/Creating_a_distributed_table/Remote_tables.md)
* [• Listing tables](Listing_tables.md)
* [• Deleting a table](Deleting_a_table.md)
* [• Emptying a table](Emptying_a_table.md)
* [⪢ Creating a cluster](Creating_a_cluster/Creating_a_cluster.md)
    * [Adding a new node](Creating_a_cluster/Adding_a_new_node.md)
    * [⪢ Remote nodes](Creating_a_cluster/Remote_nodes.md)
        * [Mirroring](Creating_a_cluster/Remote_nodes/Mirroring.md)
        * [Load balancing](Creating_a_cluster/Remote_nodes/Load_balancing.md)
    * [⪢ Setting up replication](Creating_a_cluster/Setting_up_replication/Setting_up_replication.md)
        * [Creating a replication cluster](Creating_a_cluster/Setting_up_replication/Creating_a_replication_cluster.md)
        * [Joining a replication cluster](Creating_a_cluster/Setting_up_replication/Joining_a_replication_cluster.md)
        * [Deleting a replication cluster](Creating_a_cluster/Setting_up_replication/Deleting_a_replication_cluster.md)
        * [Adding and removing a table from a replication cluster](Creating_a_cluster/Setting_up_replication/Adding_and_removing_a_table_from_a_replication_cluster.md)
        * [Managing replication nodes](Creating_a_cluster/Setting_up_replication/Managing_replication_nodes.md)
        * [Replication cluster status](Creating_a_cluster/Setting_up_replication/Replication_cluster_status.md)
        * [Restarting a cluster](Creating_a_cluster/Setting_up_replication/Restarting_a_cluster.md)
        * [Cluster recovery](Creating_a_cluster/Setting_up_replication/Cluster_recovery.md)
* [4️⃣ Connecting to the server](Connecting_to_the_server.md)
    * [MySQL protocol](Connecting_to_the_server/MySQL_protocol.md)
    * [HTTP](Connecting_to_the_server/HTTP.md)
    * [SQL over HTTP](Connecting_to_the_server/HTTP.md#SQL-over-HTTP)
* [⪢ Data creation and modification](Data_creation_and_modification/Data_creation_and_modification.md)
    * [⪢ Adding documents to a table]
        * [✔ Adding documents to a real-time table](Data_creation_and_modification/Adding_documents_to_a_table/Adding_documents_to_a_real-time_table.md)
        * [Adding rules to a percolate table](Data_creation_and_modification/Adding_documents_to_a_table/Adding_rules_to_a_percolate_table.md)
    * [⪢ Adding data from external storages]
        * [Plain tables creation](Data_creation_and_modification/Adding_data_from_external_storages/Plain_tables_creation.md)
        * [⪢ Fetching from databases]
            * [Introduction](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_databases/Introduction.md)
            * [Database connection](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_databases/Database_connection.md)
            * [Execution of fetch queries](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_databases/Execution_of_fetch_queries.md)
            * [Processing fetched data](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_databases/Processing_fetched_data.md)
            * [Ranged queries](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_databases/Ranged_queries.md)
        * [Fetching from XML stream](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_XML_streams.md)
        * [• Fetching from CSV,TSV](Data_creation_and_modification/Adding_data_from_external_storages/Fetching_from_CSV,TSV.md)
        * [• Main+delta schema](Data_creation_and_modification/Adding_data_from_external_storages/Main_delta.md)
        * [⪢ Adding data from tables]
            * [• Merging tables](Data_creation_and_modification/Adding_data_from_external_storages/Adding_data_to_tables/Merging_tables.md)
            * [• Killlists in plain tables](Data_creation_and_modification/Adding_data_from_external_storages/Adding_data_to_tables/Killlist_in_plain_tables.md)
            * [• Attaching a plain table to RT table](Data_creation_and_modification/Adding_data_from_external_storages/Adding_data_to_tables/Attaching_a_plain_table_to_RT_table.md)
            * [• Importing RT table](Data_creation_and_modification/Adding_data_from_external_storages/Adding_data_to_tables/Importing_table.md)        
        * [• Rotating a table](Data_creation_and_modification/Adding_data_from_external_storages/Rotating_a_table.md)
    * [⪢ Updating documents]
        * [• REPLACE vs UPDATE](Data_creation_and_modification/Updating_documents/REPLACE_vs_UPDATE.md)
        * [• REPLACE](Data_creation_and_modification/Updating_documents/REPLACE.md)
        * [• UPDATE](Data_creation_and_modification/Updating_documents/UPDATE.md)
    * [• Deleting documents](Data_creation_and_modification/Deleting_documents.md)
    * [• Transactions](Data_creation_and_modification/Transactions.md)
* [5️⃣ Searching]
    * [• Intro](Searching/Intro.md)
    * [⪢ Full-text matching]
        * [• Basic usage](Searching/Full_text_matching/Basic_usage.md)
        * [• Operators](Searching/Full_text_matching/Operators.md)
        * [• Escaping](Searching/Full_text_matching/Escaping.md)
        * [• Search profiling](Searching/Full_text_matching/Profiling.md)
        * [• Boolean optimization](Searching/Full_text_matching/Boolean_optimization.md)
    * [• Search results](Searching/Search_results.md)
    * [• Filters](Searching/Filters.md)
    * [• Expressions](Searching/Expressions.md)
    * [• Search options](Searching/Options.md)
    * [• Highlighting](Searching/Highlighting.md)
    * [• Sorting and ranking](Searching/Sorting_and_ranking.md)
    * [• Pagination](Searching/Pagination.md)
    * [• Distributed searching](Searching/Distributed_searching.md)
    * [• Multi-queries](Searching/Multi-queries.md)
    * [• Sub-selects](Searching/Sub-selects.md)
    * [• Grouping](Searching/Grouping.md)
    * [• Faceted search](Searching/Faceted_search.md)
    * [• Geo search](Searching/Geo_search.md)
    * [• Percolate query](Searching/Percolate_query.md)
    * [• Autocomplete](Searching/Autocomplete.md)
    * [• Spell correction](Searching/Spell_correction.md)
    * [• Query cache](Searching/Query_cache.md)
    * [• Collations](Searching/Collations.md)
    * [• Cost-based optimizer](Searching/Cost_based_optimizer.md)
    * [• K-nearest neighbor vector search](Searching/KNN.md)
* [• Updating table schema and settings](Updating_table_schema_and_settings.md)    
* [⪢ Functions](Functions.md)
    * [• Mathematical functions](Functions/Mathematical_functions.md)
    * [• Searching and ranking functions](Functions/Searching_and_ranking_functions.md)
    * [• Type casting functions](Functions/Type_casting_functions.md)
    * [• Functions to handle arrays and conditions](Functions/Arrays_and_conditions_functions.md)
    * [• Date and time functions](Functions/Date_and_time_functions.md)
    * [• Geo-spatial functions](Functions/Geo_spatial_functions.md)
    * [• String functions](Functions/String_functions.md)
    * [• Other functions](Functions/Other_functions.md)
* [⪢ Securing and compacting a table]
    * [• Backup and restore](Securing_and_compacting_a_table/Backup_and_restore.md)
    * [• Few words about RT table structure](Securing_and_compacting_a_table/RT_table_structure.md)
    * [• Flushing RAM chunk to a new disk chunk](Securing_and_compacting_a_table/Flushing_RAM_chunk_to_a_new_disk_chunk.md)
    * [• Flushing RT table to disk](Securing_and_compacting_a_table/Flushing_RAM_chunk_to_disk.md)
    * [• Compacting a table](Securing_and_compacting_a_table/Compacting_a_table.md)
    * [• Isolation during flushing and merging](Securing_and_compacting_a_table/Isolation_during_flushing_and_merging.md)
    * [• Freezing a table](Securing_and_compacting_a_table/Freezing_a_table.md)
    * [• Flushing attributes](Securing_and_compacting_a_table/Flushing_attributes.md)
    * [• Flushing hostnames](Securing_and_compacting_a_table/Flushing_hostnames.md)
* [⪢ Security]
    * [• SSL](Security/SSL.md)
    * [• Read-only](Security/Read_only.md)
* [⪢ Logging]
    * [• Query logging](Logging/Query_logging.md)
    * [• Server logging](Logging/Server_logging.md)
    * [• Binary logging](Logging/Binary_logging.md)
    * [• Docker logging](Logging/Docker_logging.md)
    * [• Rotating query and server logs](Logging/Rotating_query_and_server_logs.md)
* [⪢ Node info and management]
    * [• Node status](Node_info_and_management/Node_status.md)
    * [• SHOW META](Node_info_and_management/SHOW_META.md)
    * [• SHOW THREADS](Node_info_and_management/SHOW_THREADS.md)
    * [• SHOW QUERIES](Node_info_and_management/SHOW_QUERIES.md)
    * [• SHOW VERSION](Node_info_and_management/SHOW_VERSION.md)
    * [• KILL](Node_info_and_management/KILL.md)
    * [• SHOW WARNINGS](Node_info_and_management/SHOW_WARNINGS.md)
    * [• SHOW VARIABLES](Node_info_and_management/SHOW_VARIABLES.md)
    * [⪢ Profiling]
        * [• Query profiling](Node_info_and_management/Profiling/Query_profile.md)
        * [• Query plan](Node_info_and_management/Profiling/Query_plan.md)
    * [⪢ Table settings and status]
        * [• SHOW TABLE STATUS](Node_info_and_management/Table_settings_and_status/SHOW_TABLE_STATUS.md)
        * [• SHOW TABLE SETTINGS](Node_info_and_management/Table_settings_and_status/SHOW_TABLE_SETTINGS.md)
* [⪢ Server settings]
    * [• Searchd](Server_settings/Searchd.md)
    * [• Common](Server_settings/Common.md)
    * [• Special suffixes](Server_settings/Special_suffixes.md)
    * [• Scripted configuration](Server_settings/Scripted_configuration.md)
    * [• Comments](Server_settings/Comments.md)
    * [• Inheritance of table and source declarations](Server_settings/Inheritance_of_index_and_source_declarations.md)
    * [• Setting variables online](Server_settings/Setting_variables_online.md)
* [⪢ Integration]
    * [Logstash](Integration/Logstash.md)
    * [Filebeat](Integration/Filebeat.md)
* [⪢ Extensions]
    * [SphinxSE](Extensions/SphinxSE.md)
    * [FEDERATED](Extensions/FEDERATED.md)
    * [⪢ UDFs and Plugins](Extensions/UDFs_and_Plugins/UDFs_and_Plugins.md)
        * [Listing plugins](Extensions/UDFs_and_Plugins/Listing_plugins.md)
        * [⪢ UDF](Extensions/UDFs_and_Plugins/UDF.md)
            * [Creating a function](Extensions/UDFs_and_Plugins/UDF/Creating_a_function.md)
            * [Deleting a function](Extensions/UDFs_and_Plugins/UDF/Deleting_a_function.md)
        * [⪢ Plugins]
            * [• Creating a plugin](Extensions/UDFs_and_Plugins/Plugins/Creating_a_plugin.md)
            * [• Deleting a plugin](Extensions/UDFs_and_Plugins/Plugins/Deleting_a_plugin.md)
            * [• Enabling and disabling Buddy plugins](Extensions/UDFs_and_Plugins/Plugins/Enabling_and_disabling_buddy_plugins.md)
            * [• Reloading plugins](Extensions/UDFs_and_Plugins/Plugins/Reloading_plugins.md)
            * [• Ranker plugins](Extensions/UDFs_and_Plugins/Plugins/Ranker_plugins.md)
            * [• Token filter plugins](Extensions/UDFs_and_Plugins/Plugins/Token_filter_plugins.md)
* [• Miscellaneous tools](Miscellaneous_tools.md)
* [• OpenAPI specification](Openapi.md)
* [• Telemetry](Telemetry.md)
* [• Changelog](Changelog.md)
* [🐞 Reporting bugs](Reporting_bugs.md)
* [📖 References](References.md)
    * [• Previous versions](References.md#Documentation-for-old-Manticore-versions)