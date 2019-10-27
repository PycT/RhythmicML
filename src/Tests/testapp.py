import requests;
import json;

test_url = "http://localhost:5008/score/1";


data = \
{
    "greetings": "hello there",
    "smalltalk": "this is a test data"
};

data_json = json.dumps(data);

result = requests.post(test_url, data_json);

print(result.text);

