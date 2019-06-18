from flask import Flask, render_template;

app = Flask(__name__);
host = "0.0.0.0";
port = "5000";

#==========================================================================
@app.route("/")
def index():
    """
    On the root page models catalogue is displayed and managed.
    """
    from .helpers.get_models_list import models_list; # sets the `models_list` variable

    return render_template("index.html", title = "Catalogue", ui_caption = "Catalogue", models_list = models_list);

#==========================================================================

#==========================================================================
@app.route("/dashboard")
@app.route("/dashboard/<model_id>")
def dashboard(model_id = None):

    return render_template("dashboard.html", title = "Model Dashboard", ui_caption = "Model Dashboard", model_id = model_id);
#==========================================================================





#==========================================================================
#==========================================================================
#==========================================================================

def run_ui(app, host = host, port = port):
    """
    run_ui(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

if __name__ == "__main__":

    run_ui(app);
