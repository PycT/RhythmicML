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
    build_id integer DEFAULT 0
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