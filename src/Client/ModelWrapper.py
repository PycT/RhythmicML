# ===== default imports beginning =======
from datetime import datetime;

# =============================
# ===== custom imports beginning =======
import json;

# ======== imports end =============
# =============================

class modelWrapper:

    artifact_file_base_name = "model1";
    # here you mention all the artifacts you are going to use for predicting names
    # if it is in a subfolder to your model path, give it relative path with a subfolder
    # e.g. "wnb/wnb1.pt"

    hot_log_length = 100;
    # this is the length of a lists saving latest input and output values with timestamps

    def __init__(self, path_to_artifacts):
        """
        path_to_artifacts is a compulsory argument, never omit it in the __init__() declaration;
        it will convey a path to all files deployed to a server;
        """

        path_to_model = "{}/{}".format(path_to_artifacts, self.artifact_file_base_name);
        self.status = "Alive and kicking";
        self.inputs_hot_log = [];
        self.outputs_hot_log = [];
        self.hot_log_timestamps_stack = [];

        return None;

    def __call__(self, data):

        preprocessed_data = self.preprocess(data);
        score = self.predict(preprocessed_data);
        prediction = self.postprocess(score);

        return prediction;

    def preprocess(self, data):

        the_timestamp = datetime.datetime.now();
        timestamp_string = str(the_timestamp);

        preprocessing_result = data; # here some transformations on the data might go

        self.hot_log_timestamps_stack.append(timestamp_string);

        if len(self.inputs_hot_log) >= self.hot_log_length:
            self.inputs_hot_log.pop(0);

        self.inputs_hot_log.append(
            {
                "timestamp": timestamp_string,
                "the_data": preprocessing_result            
            });

        return preprocessing_result

    def predict(self, inputs):
        
        score = repr(inputs);

        return score;

    def postprocess(self, data):
        
        prediction = {"prediction": data};

        timestamp_string = self.hot_log_timestamps_stack.pop(0);

        if len(self.outputs_hot_log) >= self.hot_log_length:
            self.outputs_hot_log.pop(0);

        self.outputs_hot_log.append(
            {
                "timestamp": timestamp_string,
                "the_data": prediction            
            });


        prediction_json = json.dumps(prediction);

        return prediction_json;

    def lifeSign(self):
        return self.status;