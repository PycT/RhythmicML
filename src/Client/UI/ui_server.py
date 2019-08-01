from flask import Flask, render_template as renderTemplate, request;
from functools import wraps;
import json;
from . import helpers;

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

            random_string_html = \
            """
            <div align = "center" style = "padding: 32px;">
            <h1>
            {}
            </h1>
            <a href = "/">main page</a>
            </div>
            """.format( helpers.randomString() );

            return random_string_html;

    return wrapper;


#==========================================================================

#==========================================================================
#====================      UI PAGES      ============================================
#==========================================================================
@app.route("/")
def index():
    """
    On the root page models catalogue is displayed and managed.
    """
    models_list = helpers.getModelsList();
    
    print("{}/{}".format(__name__, "index"));
    #print(models_list);

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

    model_static_data = helpers.modelAllStaticData(model_id);

    print("{}/{}".format(__name__, "dashboard"));
    # print(model_static_data);

    return renderTemplate("dashboard.html", title = "Model Dashboard", ui_caption = "Model Dashboard", model_static_data = model_static_data);
#==========================================================================

#==========================================================================
#====================      HELPERS      ============================================
#==========================================================================

@app.route("/helpers/folders", methods = ["POST", "GET"])
@app.route("/helpers/folders/<template_modificator>", methods = ["POST", "GET"])
@checkPost
def helperFolders(template_modificator = "catalogue"):
    """
    /heplers/folders/<template_modificator>
    receives local folder path in POST request;
    shows the folder contents, if accessible for the user.
    template_modificator chooses the template to render the content into.
    """

    folder_contents_templates = {
        "catalogue": "folder_contents_catalogue.html",
        "dashboard": "folder_contents_dashboard.html"
    };

    data_json = request.data.decode();
    data = json.loads(data_json);

    # print("{}, {}".format(__name__, "helperFolders"));
    # print("==================");
    # print(data);
    # print("==================");

    the_folder = data["the_folder"];

    if "look_level_above" in data:
        look_level_above = data["look_level_above"];
    else:
        look_level_above = True;

    folder_contents = helpers.scanFolder(the_folder, look_level_above = look_level_above);

    if folder_contents.__class__ == str: #the decorator returns an error message, if folderScan() execution fails
        return folder_contents;

    return renderTemplate(folder_contents_templates[template_modificator], folder_contents = folder_contents, the_folder = the_folder);
#==========================================================================

#==========================================================================
@app.route("/helpers/folder_name_to_model_name", methods = ["POST", "GET"])
@checkPost
def helperFolderNameToModelName():
    """
    /helpers/foldername2modelname
    receives a path user picked path
    and returns a unique model name suggestion.
    """

    the_folder = request.data.decode();

    folder_base_name = helpers.getNameFromPath(the_folder);
    suggested_model_name = helpers.uniqueName(folder_base_name);

    return suggested_model_name;
#==========================================================================

#==========================================================================
@app.route("/helpers/add_new_model", methods = ["POST", "GET"])
@checkPost
def addModel():

    # model_name = request.data.model_name.decode();
    # the_folder = request.data.model_path.decode();

    data_json = request.data.decode();

    data = json.loads(data_json);

    new_model_name = data["model_name"];
    new_model_path = data["model_path"].replace(" ", "\\ ");

    execution_status = helpers.addNewModel(new_model_name, new_model_path);

    return execution_status;

#==========================================================================
#==========================================================================
#==========================================================================

def runUI(app, host = helpers.configuration.host, port = helpers.configuration.port):
    """
    run_ui(app, host = host, port = port):  
    app is a Flask app
    """

    app.run(debug = True, host = host, port = port);

    return True;

if __name__ == "__main__":

    runUI(app);
