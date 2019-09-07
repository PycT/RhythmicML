from flask import Flask, request;
from . import helpers;
from functools import wraps;
import json;

app = Flask(__name__);

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

    result = helpers.deployModel(request.files);
    request.close();
    result_json = json.dumps(result);

    return result_json;

#==========================================================================
#==========================================================================
#==========================================================================

def runAPI(app, host = helpers.configuration.host, port = helpers.configuration.port):
    """
    run_ui(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

    return True;

if __name__ == "__main__":

    runAPI(app);
