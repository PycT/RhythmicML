import sqlite3;

db_filename = ".db.sqlite3";

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
CREATE TABLE IF NOT EXISTS models
(
    id integer PRIMARY KEY,
    model_name text NOT NULL UNIQUE,
    model_description text,
    initial_metada text
);
""";

model_versions_table = \
"""
CREATE TABLE IF NOT EXISTS versions
(
    id integer PRIMARY KEY,
    model_id integer NOT NULL,
    version integer NOT NULL DEFAULT 0,
    metadata text,
    commit_comment text NOT NULL,
    FOREIGN KEY (model_id) REFERENCES models (id) 
);
""";


def faultHandler(func):

    def wrapper(*args, **kwargs):

        try:
            func(*args, **kwargs);
            return True;

        except Exception as error_message:
            print("Something went wrong: {}".format(error_message));
            return False;

    return wrapper;

def dbConnect(db_filename = db_filename):

    try:
        db_connection = sqlite3.connect(db_filename);
        db_cursor = db_connection.cursor();

        return db_connection, db_cursor;

    except Exception as error_message:
        print("Something went wrong: {}".format(error_message));
        
        return False, False;

@faultHandler
def dbExecute(db_cursor, db_request):
        db_cursor.execute(db_request);

@faultHandler
def createTables(db_cursor):

    dbExecute(db_cursor, general_table);
    dbExecute(db_cursor, models_table);
    dbExecute(db_cursor, model_versions_table);

def main():

    db_connection, db_cursor = dbConnect();

    if db_connection:
        createTables(db_cursor);
        db_connection.commit();
        db_connection.close();

        print("Database created, tables created.")
    else:
        print("db connection failed.");
        exit(4);

if __name__ == "__main__":
    main();