from rhythmic.general import faultReturnHandler;
from rhythmic.db import SQLiteDB;
from os.path import exists;
from os import remove;
from . import configuration, unpackVersion, scanModelFolder, filePropertiesDictionary;

def setModelVersionActive(data):

    model_version_archive_file_name = "{}/{}/model_{}_ver{}.zip".\
    format(
                    data["model_path"],
                    configuration.storage_folder_name,
                    data["model_id"],
                    data["desired_version_number"]
                );

    if not exists(model_version_archive_file_name):
        return "No stored version {} package found. Activation cancelled.".format(data["desired_version_number"]);

    files_to_purge = scanModelFolder(data["model_path"]);
    for filename in files_to_purge:
        remove(filename);

    unpackVersion(model_version_archive_file_name, data["model_path"]);

    # we have now to udate last_modified timestamps so system would not identify freshly unpacked files as modified.
    # to minimize db queries, we'll just rewrite existinf rows in files_table.
    # but first we'll set proper active_version for the model to perform al db operations in one ocntext.
    with SQLiteDB(configuration.db_file_name) as db:
        db.execute(
            """
            UPDATE models_table SET active_version = '{}' WHERE id = '{}';
            """.format(
                                data["desired_version_number"],
                                data["model_id"]
                            )
            );

        existing_files_records = db.execute(
            """
            SELECT * FROM files_table WHERE model_version_id = '{}';
            """.format(
                                data["desired_version_id"]
                            )
            );

        version_files_data = {};

        for the_record in existing_files_records:
            version_file_properties = filePropertiesDictionary(the_record);
            
            if (version_file_properties["is_deployed"]):
                is_deployed = 1;
            else:
                is_deployed = 0;

            version_files_data[ version_file_properties["absolute_path"] ] = \
                {
                    "file_commit_state": version_file_properties["file_commit_state"],
                    "is_deployed": is_deployed
                }

        db.execute(
            """
            DELETE FROM files_table WHERE model_version_id = '{}';
            """.format(
                                data["desired_version_id"]
                            )
            );

        files_record_request = \
        """
        INSERT INTO files_table
        (
            model_version_id,
            absolute_path,
            file_commit_state,
            last_modified_time,
            is_deployed
        )
        VALUES
        """;
        active_version_files = scanModelFolder(data["model_path"]);

        if len(active_version_files) > 0:
            files_record_values = "";

            for item_path in active_version_files:
                item = active_version_files[item_path];
                files_record_values += \
                "('{}', '{}', '{}', '{}', '{}'), \n".format(
                                                                data["desired_version_id"],
                                                                item_path,
                                                                version_files_data[item_path]["file_commit_state"],
                                                                item["last_modified_time"],
                                                                version_files_data[item_path]["is_deployed"]
                                                            );

            files_record_request += files_record_values[:len(files_record_values) -3] + ";"; #truncating `, \n` from the end of request and adding `;`.

            db.execute(files_record_request);
        


    return "Success";