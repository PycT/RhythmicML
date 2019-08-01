"""
This helper  returns dictionaries of all versions and all the files of all versions of particular model with all the metadata stored.
In other words it returns the whole tree of model related static entities.
"""

from rhythmic.db import SQLiteDB;
from rhythmic.general import faultReturnHandler;
from . import modelPropertiesDictionary, versionPropertiesDictionary, filePropertiesDictionary;
from . import configuration;

@faultReturnHandler
def modelAllStaticData(model_id):

    all_model_info = \
    {
        "properties": {},
        "model_versions": {}
    };

    with SQLiteDB( configuration.db_file_name) as db:
        
        model_properties = db.execute(
            """
            SELECT * FROM models_table WHERE id = '{}';
            """.format(model_id)
            );

        # print("=====================");
        # print(model_properties[0]);
        # print("=====================");

        all_model_info["properties"] = modelPropertiesDictionary(model_properties[0]);

        # print("=====================");
        # print(all_model_info);
        # print("=====================");

        model_versions = db.execute(
            """
            SELECT * FROM versions_table WHERE model_id = '{}' ORDER BY version DESC;
            """.format(model_id)
            );

        for model_version in model_versions:

            version_properties = versionPropertiesDictionary(model_version);

            version_files = {};

            version_tracked_files = db.execute(
                """
                SELECT * FROM files_table WHERE model_version_id = '{}' ORDER BY file_path ASC;
                """.format(version_properties["id"])
                );

            for version_tracked_file in version_tracked_files:

                version_tracked_file_data = filePropertiesDictionary(version_tracked_file);

                version_files_key = version_tracked_file_data["file_path"];
                version_files[ version_files_key ] = version_tracked_file_data;

            model_versions_key = version_properties["version"];
            all_model_info["model_versions"][model_versions_key] = \
                {
                    "version_properties": version_properties,
                    "version_files": version_files
                };

    return all_model_info;