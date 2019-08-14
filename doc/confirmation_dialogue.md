#Confirmation Dialogue

For sensitive actions requiring confirmation, there is a `confirmation_dialogue_canvas` and `confirmaition_dialogue` containers  designated in general layout template.

##Workflow

When a confirmation required for action, you call `callConfirmationDialogue()` defined in `manipulations.js`.
This method requires the following parameters:

+ confirmation_message - string with a message to show in dialogue. E.g. "are you sure?"
+ helper_url - string, an url to send request with data to, if `Yes` button is pressed;
+ data_for_helper - string, data to send with that request
+ confirmation_result - string: 
+      "refresh" - call asyncPostRequestWithRefresh(): `Yes` button will send POST request to given URL and refresh the page on success (200). This is the default option.
+      "value" - call asyncPostRequest(..., to_innerHTML = false): `Yes` button will send POST request to given URL and assign returned value to given DOM element (see `result_element_id` below);
+      "html" - call regular asyncPostRequest():  `Yes` button will send POST request to given URL and put returned resukt to given DOM element innerHTML (see `result_element_id` below);
+ result_element_id - string, dom element id to use in "value" and "html" cases.


```function callConfirmationDialogue(confirmation_message, helper_url, data_for_helper, confirmation_result = "refresh", result_element_id = "status_bar")
```