from rhythmic.db import SQLiteDB;

db_filename = ".rhml_db.sqlite3";

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
    file_checksum text,
    FOREIGN KEY (model_version_id) REFERENCES versions_table (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);
""";

def main():

    with SQLiteDB(db_filename) as db:

        db.runScript(
            general_table +
            models_table +
            model_versions_table +
            model_files_table
            );

    print("Database is created, tables are created.")

if __name__ == "__main__":
    main();