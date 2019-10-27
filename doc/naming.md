# Coding naming conventions
* variables are lowercase, words separated with underscore
* functions are camelcase, starting with lowercase
* classes are camelcase, starting with capital letter

# Files and folders naming conventions

* model version archive file name built as follows: "model_" + `model_id` + "_ver" + `version_number` + ".zip"
* package to send for deploy file name built as follows: "deploy_" + `model_id` + "_" + `deploy_id` + ".zip"
* folder on a serving host with model artifacts named as follows: "model" + `deploy_id`