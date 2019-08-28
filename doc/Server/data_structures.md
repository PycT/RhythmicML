# DB Tables
```
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

```

## Serving Cell inputs and outputs snapshot

```
cell_snapshot = {
                            `trace_id` : {
                                                "input": `input`,
                                                "output": `output`
                                                }

                            ..

                            `trace_id` : {
                                                "input": `input`,
                                                "output": `output`
                                                }
                          }
```