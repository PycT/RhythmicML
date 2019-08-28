from flask import send_file, safe_join;
from .packer import packFiles;
import json;

def deployModel(data):
    """
    var data = 
    {
        "deploy_url": window.actual_deploy_destination,
        "model_name": window.the_model_name,
        "model_id": window.the_model_id,
        "version_number": window.active_version_number,
        "version_id": window.active_version_id,
        "files_data": window.active_version_files_data
    }
    """

    return "1Success";