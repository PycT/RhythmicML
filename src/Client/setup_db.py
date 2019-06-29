from rhythmic.db import SQLiteDB;
from datetime import datetime;
from UI import configuration;

db_file_name = configuration["db_file_name"];

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
    last_version integer NOT NULL DEFAULT 0,
    last_version_timestamp text NOT NULL,
    deploy_destination text,
    model_description text,
    initial_metada text
);
""";

model_versions_table = \
"""
CREATE TABLE IF NOT EXISTS versions_table
(
    id integer PRIMARY KEY,
    model_id integer NOT NULL,
    version integer NOT NULL DEFAULT 0,
    metadata text,
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
    file_path text NOT NULL,
    file_commit_state text NOT NULL DEFAULT 'new',
    last_modified_time text NOT NULL,
    is_deployed integer NOT NULL DEFAULT 1,
    FOREIGN KEY (model_version_id) REFERENCES versions_table (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);
""";

# file_commit_state a state of file by commit moment; soptions: new, same, changed, deleted

def main():

    with SQLiteDB(db_file_name) as db:

        db.runScript(
            general_table +
            models_table +
            model_versions_table +
            model_files_table
            );

    print(   "Database is created, tables are created. DB file: \"{}\", {}".format(  configuration["db_file_name"], str( datetime.now() )  )   );

if __name__ == "__main__":
    main();