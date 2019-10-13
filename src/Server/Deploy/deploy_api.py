from flask import Flask, request;
from . import helpers;
from functools import wraps;
import json;
# from subprocess import Popen, PIPE;
from os import getcwd as getCurrentWorkingDir;

app = Flask(__name__);

# working_dir_path = getCurrentWorkingDir();
# storage_dir = "{}/{}".format(working_dir_path, helpers.configuration.storage_folder_name);

deploy_storage = helpers.DeployMemoryStorage();

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
#====================      SERVER ROUTES     ========================================
#==========================================================================

@app.route("/deploy", methods = ["POST"])
@checkPost
def deployModelData():

    global deploy_storage;

    result = helpers.deployModel(request.files);
    request.close();
    result_json = json.dumps(result);

    model_deploy_id = result["model_deploy_id"];

    deploy_storage.deployCell(model_deploy_id);

    ###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # importlib.reload! https://docs.python.org/3/library/importlib.html#importlib.import_module
    ###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # --if model_deploy_id in models_processes:
    # --   models_processes[model_deploy_id].kill();

    # -- models_processes[model_deploy_id] = Popen(["python", "model_cell.py", str(model_deploy_id)], stdin = PIPE, stdout = PIPE, stderr = PIPE);

    return result_json;

@app.route("/score/<model_deploy_id>", methods = ["POST"])
@checkPost
def scoreModel(model_deploy_id):

    global deploy_storage;

    data_json = request.data.decode();
    the_model = deploy_storage.fetchCell(model_deploy_id);
    result_json = the_model(data_json);

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
