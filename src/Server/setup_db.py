from rhythmic.db import SQLiteDB;
from datetime import datetime;
from Deploy import configuration;

db_file_name = configuration.db_file_name;

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
    last_deploy_timestamp text NOT NULL,
    active_version integer NOT NULL DEFAULT 0,
    deploy_id integer DEFAULT 0
);
""";

model_files_table = \
"""
CREATE TABLE IF NOT EXISTS files_table
(
    id integer PRIMARY KEY,
    model_id integer NOT NULL,
    relative_path text NOT NULL,
    is_deployed integer NOT NULL DEFAULT 1,
    FOREIGN KEY (model_id) REFERENCES models_table (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);
""";

# file_commit_state a state of file by commit moment; options: new, same, modified

def main():

    with SQLiteDB(db_file_name) as db:

        db.runScript(
            general_table +
            models_table +
            model_files_table
            );

    print(   "Database is created, tables are created. DB file: \"{}\", {}".format(  configuration.db_file_name, str( datetime.now() )  )   );

if __name__ == "__main__":
    main();