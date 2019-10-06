from flask import Flask, request;
from . import helpers;
from functools import wraps;
import json;
# from subprocess import Popen, PIPE;
from os import getcwd as getCurrentWorkingDir;

app = Flask(__name__);

models_cells = {};
working_dir_path = getCurrentWorkingDir();
storage_dir = "{}/{}".format(working_dir_path,configuration.storage_folder_name);

#==========================================================================
#====================      DECORATORS     =========================================
#==========================================================================
def checkPost(entry_point):

    @wraps(entry_point)
    def wrapper(*args, **kwargs):
        if request.method == "POST":

            return entry_point(*args, **kwargs);

        else:

            return "Only POST requests are presumed.";

    return wrapper;

#==========================================================================
#====================     LOCAL HELPERS    =========================================
#==========================================================================

def redeploy(model_deploy_id, model_cells = model_cells, storage_dir = storage_dir):
    """

    """
    deploy_dir = "{}/model{}".format(storage_dir, model_deploy_id);
    if model_deploy_id in model_cells:
        pass;

    return None;

#==========================================================================
#====================      SERVER ROUTES     ========================================
#==========================================================================

@app.route("/deploy", methods = ["POST"])
@checkPost
def deployModelData():

    global models_processes;

    result = helpers.deployModel(request.files);
    request.close();
    result_json = json.dumps(result);

    model_deploy_id = result["model_deploy_id"];

    ###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # importlib.reload! https://docs.python.org/3/library/importlib.html#importlib.import_module
    ###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # --if model_deploy_id in models_processes:
    # --   models_processes[model_deploy_id].kill();

    # -- models_processes[model_deploy_id] = Popen(["python", "model_cell.py", str(model_deploy_id)], stdin = PIPE, stdout = PIPE, stderr = PIPE);

    return result_json;

@app.route("/score/<model_deploy_id>", methods = ["POST"])
@checkPost
def scoreModel(model_deploy_id, data_json):

    global models_processes;

    if model_deploy_id in models_processes:
        result = {"1": "pew"};
        # outs, errs = proc.communicate(input = data_json)
    else:
        try:
            models_processes[model_deploy_id] = Popen(["python", "model_cell.py", str(model_deploy_id)], stdin = PIPE, stdout = PIPE, stderr = PIPE);
            result = {"1": "pew"};
        except Exception as error_message:
            result = {"Status": "{}".format(error_message)} 

    result_json = json.dumps(result);

    return result_json;

#==========================================================================
#==========================================================================
#==========================================================================

def runAPI(app, host = helpers.configuration.host, port = helpers.configuration.port):
    """
    runAPI(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

    return True;

if __name__ == "__main__":

    runAPI(app);
