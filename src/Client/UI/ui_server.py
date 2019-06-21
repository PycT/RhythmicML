from flask import Flask, render_template as renderTemplate, request;

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

    return renderTemplate("index.html", title = "Catalogue", ui_caption = "Catalogue", models_list = models_list);

#==========================================================================

#==========================================================================
@app.route("/dashboard")
@app.route("/dashboard/<model_id>")
def dashboard(model_id = None):
    """
    /dashboard/<model_id>
    This is a particular model's dashboard, rendered with id.
    """

    return renderTemplate("dashboard.html", title = "Model Dashboard", ui_caption = "Model Dashboard", model_id = model_id);
#==========================================================================

@app.route("/folders", methods = ["POST"])
def folders():
    """
    /folders/
    receives local folder path in POST request;
    shows the folder contents, if accessible for the user.
    """

    if request.method == "POST":

        the_folder = request.data.decode();

        from .helpers.folder_scan import scanFolder;

        folder_contents = scanFolder(the_folder);

        if folder_contents.__class__ == str: #the decorator returns an error message, if folderScan() execution fails
            return folder_contents;

        return renderTemplate("folder_contents.html", folder_contents = folder_contents, the_folder = the_folder);

    else:

        return "Go away."

#==========================================================================
#==========================================================================
#==========================================================================

def runUI(app, host = host, port = port):
    """
    run_ui(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

if __name__ == "__main__":

    runUI(app);
