from flask import Flask, render_template;

app = Flask(__name__);
host = "0.0.0.0";
port = "5000";


@app.route("/")
def indexpage():

    return render_template("index.html", title = "Catalogue", ui_caption = "Catalogue");




if __name__ == "__main__":

    app.run(debug = True, host = host, port = port);