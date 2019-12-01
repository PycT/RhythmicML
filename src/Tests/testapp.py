import requests;
import json;

test_url = "http://localhost:5008/score/1";
test_status_url = "http://localhost:5008/status/1";


data = \
{
    "greetings": "hello there",
    "smalltalk": "this is a test data"
};

data_json = json.dumps(data);

# result = requests.post(test_url, data_json);

# print(result.text);

print("Checking status:");

#status = requests.post(test_status_url);
status = requests.get(test_status_url);
print(status.status_code);
#print(status.text);
