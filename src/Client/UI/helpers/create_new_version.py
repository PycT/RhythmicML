from rhythmic.general import faultReturnHandler;
from rhythmic.db import SQLiteDB;
from . import configuration;
from .packer import packFiles;
from .random_string import randomString;

@faultReturnHandler
def createNewVersion(data):

    #================= finished DB work =====================================

    model_storage_path = data["model_path"] + "/{}".format(configuration.storage_folder_name);
    print(model_storage_path);
    # if ( (not exists(model_storage_path)) or (not isDir(model_storage_path)) ):
    #     makeDir(model_storage_path);

    #================= Starting  building ver0 .zip in storage =====================================

    # archive_name = model_storage_path + "/model_{}_ver{}.zip".format(new_model_id, new_version_number);

    # packFiles(model_path, archive_name, new_model_files);

    #================= Finished building ver0 .zip in storage =====================================

    return randomString();