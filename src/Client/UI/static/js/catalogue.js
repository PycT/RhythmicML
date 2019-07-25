"use strict";

//toggleDisplay(), setVisible(), setInvisible() are defied in manipulations.js
//asyncPostRequest(), asyncPostRequestWithRefresh() are defined in async_requests.js

function initOnLoad()
{
    document.folder_picked = false;
    //document.getElementById('model_name_input_container').style.display = 'none';
    document.getElementById('new_model_name').value = "";
    document.getElementById('new_model_path').value = "~";
    return true;
}

function onCancelNewModelSubmitButtonClick()
{
    toggleDisplay('catalogue_toolbox_regular');
    toggleDisplay('catalogue_toolbox_add_model');
    initOnLoad();
    return true;
}

function onAddInvocationButtonClick()
{
    toggleDisplay('catalogue_toolbox_regular');
    toggleDisplay('catalogue_toolbox_add_model');
    var data = {"the_folder": "~"};
    var data_json = JSON.stringify(data);
    asyncPostRequest('/helpers/folders/catalogue', data_json, 'new_model_folder');
    return true;
}

// function onPickModelFolderButtonClick()
// {
//     setInvisible('pick_the_folder_button');
//     setInvisible('the_folder_items_list');
//     setVisible('model_name_input_container');
//     return true;
// }

function pickFolder(local_folder)
{
    if (document.getElementById("name_the_model_by_folder").checked)
    {
        asyncPostRequest('/helpers/folder_name_to_model_name', local_folder, 'new_model_name', false);
    }
    document.folder_picked = true;

    return true;
}

function onAddModelButtonClick()
{
    
    if (!document.folder_picked)
    {
        alert("Pick a folder, containing your model!");
        return false;
    }

    if (document.getElementById("new_model_name").value == "")
    {
        alert("Specify your model's name!");
        return false;
    }

    var new_model_name = document.getElementById("new_model_name").value;
    var new_model_path = document.getElementById("new_model_path").value;

    var data = {model_name: new_model_name, model_path: new_model_path};
    var data_json = JSON.stringify(data);

    asyncPostRequestWithRefresh("/helpers/add_new_model", data_json, "status_bar");

    toggleDisplay('catalogue_toolbox_regular');
    toggleDisplay('catalogue_toolbox_add_model');

    initOnLoad();

    return true;
}

function onSearchInputChange(the_value)
{
    if (the_value == "")
    {
        models_array.forEach( function(item)
        {
            setVisible('model'+item.id, 'table-row');
            setVisible('model_path'+item.id, 'table-row');
        });
        return true;
    }

    var the_pattern = the_value.toLowerCase();

    models_array.forEach( function(item)
    {
        if ( (item.name.includes(the_pattern)) || (item.path.includes(the_pattern)) )
        {
            setVisible('model'+item.id, 'table-row');
            setVisible('model_path'+item.id, 'table-row');
        }
        else
        {
            setInvisible('model'+item.id, 'table-row');
            setInvisible('model_path'+item.id, 'table-row');
        }
    });
}
