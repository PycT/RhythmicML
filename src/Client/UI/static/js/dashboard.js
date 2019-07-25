"use strict";

//toggleDisplay(), setVisible(), setInvisible() are defied in manipulations.js
//asyncPostRequest(), asyncPostRequestWithRefresh() are defined in async_requests.js

function scanFolder(the_folder, ceiling = "")
{
    var look_level_above = true;

    if (the_folder == ceiling)
    {
        look_level_above = false;
    }
    
    var data = {
                        "the_folder": the_folder,
                        "look_level_above": look_level_above
                      };
    var data_json = JSON.stringify(data);
    asyncPostRequest('/helpers/folders/dashboard', data_json, 'model_folder');
}