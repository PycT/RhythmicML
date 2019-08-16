# DB Tables
general_table = \
"""
CREATE TABLE IF NOT EXISTS general
(
    id integer PRIMARY KEY,
    param_key text NOT NULL,
    param_value text NOT NULL
);
""";

models_table = \
"""
CREATE TABLE IF NOT EXISTS models_table
(
    id integer PRIMARY KEY,
    model_name text NOT NULL UNIQUE,
    model_path text NOT NULL UNIQUE,
    last_version_timestamp text NOT NULL,
    last_version integer NOT NULL DEFAULT 0,
    active_version integer NOT NULL DEFAULT 0,
    deploy_destination text DEFAULT "http://localhost:5008",
    deploy_status integer DEFAULT 0
);
""";

model_versions_table = \
"""
CREATE TABLE IF NOT EXISTS versions_table
(
    id integer PRIMARY KEY,
    model_id integer NOT NULL,
    version integer NOT NULL DEFAULT 0,
    metadata text DEFAULT 'Description: \nDataset: \nTraining Epochs: \nLearning Rate: \nBatch Size: ',
    commit_comment text NOT NULL,
    created_timestamp text NOT NULL,
    FOREIGN KEY (model_id) REFERENCES models_table (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);
""";

model_files_table = \
"""
CREATE TABLE IF NOT EXISTS files_table
(
    id integer PRIMARY KEY,
    model_version_id integer NOT NULL,
    absolute_path text NOT NULL,
    file_commit_state text NOT NULL DEFAULT 'new',
    last_modified_time text NOT NULL,
    is_deployed integer NOT NULL DEFAULT 1,
    FOREIGN KEY (model_version_id) REFERENCES versions_table (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);
""";

# Properties of entities
## Model
properties_dictionary = \
    {
        "id": sql_raw_list[0],
        "name": sql_raw_list[1],
        "path": sql_raw_list[2],
        "last_version_timestamp": sql_raw_list[3],
        "last_version": sql_raw_list[4],
        "active_version": sql_raw_list[5],
        "deploy_destination": sql_raw_list[6],
        "deploy_status": sql_raw_list[7]
    };

## Version
properties_dictionary = \
    {
        "id": sql_raw_list[0],
        "model_id": sql_raw_list[1],
        "version": sql_raw_list[2],
        "metadata": sql_raw_list[3],
        "commit_comment": sql_raw_list[4],
        "created_timestamp": sql_raw_list[5]
    };


## File
properties_dictionary = \
    {
        "id": sql_raw_list[0],
        "model_version_id": sql_raw_list[1],
        "absolute_path": sql_raw_list[2],
        "file_commit_state": sql_raw_list[3], //file_commit_state is a state of file by commit moment; options: new, same, modified
        "last_modified_time": sql_raw_list[4],
        "is_deployed": is_deployed
    }

# Model static data (Dashboard)

model_static_data
{
    properties:
    {
        id: "...",
        name: "...",
        path: "...",
        last_version_timestamp: "...",
        last_version: "...",
        active_version: "...",
        deploy_destination: "...",
        deploy_status: "..."
    },
    model_versions:
    {
        `version_number`: 
        {
            version_properties:
            {
                id: "...",
                model_id: "...",
                version: "...",
                metadata: "...",
                commit_comment: "...", //(not used currently)
                created_timestamp: "..."
            },
            version_files:
            {
                `file_absolute_path`:
                {
                    id: "...",
                    model_version_id: "...",
                    file_path: "...",
                    file_commit_state: "...", //file_commit_state is a state of file by commit moment; options: new, same, modified
                    last_modified_time: "...",
                    is_deployed: "..."
                },
                ..
                `file_absolute_path`:
                {
                    ..
                }
            },
            changed_folders: *//this field is present for active model version only*
            [
                '`folder_absolute_path`', .., '`folder_absolute_path`'
            ]
            absent_files:  *//this field is present for active model version only*
            {
                `folder_absolute_path`:
                [
                    '`file_base_name`', .., '`file_base_name`'
                ]
            },
            modified_files: *//this field is present for active model version only*; used when creating incremented version;
            [
                '`file_absolute_path`', .., '`file_absolute_path`'
            ]
        },
        ..
        `version_number`:
        {
            ..
        }
    }
}

# Version Update
var data = 
{
    "model_path": window.model_path,
    "files_tracker": passed_files_data,
    "modified_files": window.active_version_modified_files,
    "model_id": window.the_model_id,
    "new_version_number": window.last_version + 1,
    "metadata": encodeURI(actual_metadata)
}
