"use strict";

function callConfirmationDialogue(confirmation_message, helper_url, data_for_helper, confirmation_result = "refresh", result_element_id = "status_bar")
// confirmation dialogue parameters are the following:
// confirmation_message - string, the statement to confirm
// helper_url - string, an url to request if confirmation is positive
// data_for_helper - string, data to send with that request
// confirmation_result - string: 
//      "refresh" - call asyncPostRequestWithRefresh
//      "value" - call asyncPostRequest(..., to_innerHTML = false)
//      "html" - call regular asyncPostRequest();
// result_element_id - string, dom element id to use in "value" and "html" cases
{
    var dialogue_data = {
        "confirmation_message": confirmation_message,
        "helper_url": helper_url,
        "data_for_helper": data_for_helper,
        "confirmation_result": confirmation_result,
        "result_element_id": result_element_id
    }
    setVisible("confirmation_dialogue_canvas");
    scrollIntoView("confirmation_dialogue_canvas");
    var data_json = JSON.stringify(dialogue_data);
    asyncPostRequest("/helpers/confirmation_dialogue", data_json, "confirmation_dialogue");
}