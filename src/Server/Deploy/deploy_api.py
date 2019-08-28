from flask import Flask, request;
from .helpers import configuration;

app = Flask(__name__);

#==========================================================================
#==========================================================================
#==========================================================================

@app.route("/settle", methods = ["POST"])
def settleModel():

    return True;

#==========================================================================
#==========================================================================
#==========================================================================

def runAPI(app, host = configuration.host, port = configuration.port):
    """
    run_ui(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

    return True;

if __name__ == "__main__":

    runAPI(app);
