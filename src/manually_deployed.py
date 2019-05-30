from flask import Flask, request;
import keras;
from tensorflow import get_default_graph;
from PIL import Image;
import base64, io;

app = Flask(__name__);
host = "0.0.0.0";
port = 5002;

model_path = "../../../researches/retina_kaggle/models/kaggle_retinopathy_299_0.0.h5";


def init():

    model = keras.models.load_model(model_path);
    graph = get_default_graph();

    return model, graph;

def preprocess(data):
    """
    This method decodes base64 encoded image, resizes it to 299 x 299 shape,
    and turns it into tensor digestable by the model
    """

    decoded_image = base64.b64decode(data);
    image = Image.open(io.BytesIO(decoded_image));

    resized_image = image.resize((299, 299));

    tensor = keras.preprocessing.image.img_to_array(resized_image);

    reshaped_tensor = tensor.reshape((1,) + tensor.shape);

    return reshaped_tensor;

def postprocess(data):

    classes = \
    {
        0: "No_DR",
        1: "Mild_DR",
        2: "Moderate_DR",
        3: "Severe_DR",
        4: "Proliferative_DR"
    };

    result = classes[ data.argmax() ];

    return result;

@app.route("/score/", methods = ["POST"])
def score():
    
    global model, graph;

    if request.method == "POST":

        with graph.as_default():

            input_tensor = preprocess(request.data);
            prediction = model.predict(input_tensor);

        return postprocess(prediction);

    return "abnormal request";

@app.route("/lifesign/")
def lifeSign():
    return "I am alive and kicking, thank you."

if __name__ == "__main__":
    
    global model, graph;
    model, graph = init();
    app.run(debug = True, host = host, port = port);