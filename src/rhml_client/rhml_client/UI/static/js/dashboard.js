"use strict";

//toggleDisplay(), setVisible(), setInvisible(), document.getElementById(), enableElement(), inputValueHasChanged()
// elementIsDisabled()
// and other manipulations with DOM are defied in manipulations.js
//
//asyncPostRequest(), asyncPostRequestWithRefresh() are defined in async_requests.js
// 
// 
//------
//window.current_folder_contents - scanned folder contents
//window.active_version_files_data - db snapshot
//window.active_version_files_data_tracker - to track user made changes
//------
//<button id = "action" disabled>Save All as v. {{model_static_data["properties"]["last_version"] + 1}}</button> -
// - activate it if any changes detected


//=======================================================================
//=========================               UI             ==================================
//=======================================================================

function markFileChange(absolute_path)
{
    var folder_item = document.getElementById("folder_item_"+absolute_path);
    folder_item.style.fontWeight = "bolder";
    folder_item.style.backgroundColor = "#fafada";
    folder_item.style.color = "#cc0000";
}

function markNewFile(absolute_path)
{
    var folder_item = document.getElementById("folder_item_"+absolute_path);
    folder_item.style.fontWeight = "bolder";
    folder_item.style.backgroundColor = "#fafada";
    folder_item.style.color = "#000000";
    var delete_button_id = "delete_button_"+ absolute_path;
    if (!document.getElementById(delete_button_id))
    {
        folder_item.innerHTML += "<button class = 'small_button' id = '"+ delete_button_id +
        "' onclick = 'deleteFile(\"" + absolute_path + "\");'> Delete </button>";
    }
}

function resetFileMark(absolute_path)
{
    var folder_item = document.getElementById("folder_item_"+absolute_path);
    folder_item.style.fontWeight = "";
    folder_item.style.backgroundColor = "";
    folder_item.style.color = "";
}

function recordFolderTouch(the_folder)
{
    var is_fresh = false;
    if (!window.touched_folders.includes(the_folder))
    {
        window.touched_folders.push(the_folder);
        is_fresh = true;
    }

    return is_fresh;
}

function setFolderItemMark(absolute_path)
//color changes and set checkboxes in accordance with db records
{
    var change_detected = false;

    if ( window.current_folder_contents.hasOwnProperty(absolute_path) && 
        !window.current_folder_contents[absolute_path]["is_dir"])
    //we are looking onto files here
    {
        var item = window.current_folder_contents[absolute_path];

        if (window.active_version_files_data_tracker.hasOwnProperty(absolute_path))
        //if the file is tracked
        {
            if (!window.active_version_files_data.hasOwnProperty(absolute_path))
            //if the file was not tracked when the version was created - change happened
            {
                change_detected = true;
            }
            else
            //if it was - let us check system 'last modfied' file attribute
            {
                if (item["last_modified_time"] != window.active_version_files_data_tracker[absolute_path]["last_modified_time"])
                {
                    change_detected = true;
                }
            }

            if (window.active_version_files_data.hasOwnProperty(absolute_path) &&
                window.active_version_files_data_tracker[absolute_path]["is_deployed"] != 
                window.active_version_files_data[absolute_path]["is_deployed"])
            //was it marked as deployable when the version was created?
            {
                change_detected = true;
            }

        }
        else
        //if the file is not tracked
        {
            if (window.active_version_files_data.hasOwnProperty(absolute_path))
            //was it tracked when the version was created?
            {
                change_detected = true;
            }
        }

        if (change_detected)
        {
            markFileChange(absolute_path);
        }
        else
        {
            resetFileMark(absolute_path);
            if (!window.active_version_files_data.hasOwnProperty(absolute_path))
            {
                markNewFile(absolute_path);
                //change_detected = true;
            }
        }

    }

    return change_detected;
}

function setFolderContentMarks()
//color changes and set checkboxes in accordance with db records
{
    var change_detected = false;
    if (window.active_version_deleted_files.hasOwnProperty(window.the_folder))
    {
        change_detected = true;
        var folder_items_table = document.getElementById("the_folder_items_list");
        window.active_version_deleted_files[window.the_folder].forEach(
            function(deleted_file)
            {
                var deleted_file_path = window.the_folder + '/' + deleted_file;
                var item_row = "<tr class = 'folder_content_box_item'>\
                <td class = 'dashboard_deleted_file'>" + deleted_file + " <sup>deleted</sup></td><td colspan = '2' align = 'center'>\
                <button class = 'small_button' onclick = 'restoreFile(\"" + deleted_file_path + "\");'>Restore</button>\
                </td></tr>";

                folder_items_table.innerHTML += item_row;
            });
    }

    for (var item_record in window.current_folder_contents)
    {
        if ( window.current_folder_contents.hasOwnProperty(item_record) )
        {
            var base_name_cell = document.getElementById('base_name_' + item_record);
            var base_name = base_name_cell.innerHTML;

            if (window.current_folder_contents[item_record]["is_dir"])
            {
                if (window.active_version_changed_folders.includes(item_record))
                {
                    base_name_cell.innerHTML +=  "<sup style = 'color: red;'> untracked/modified </sup>";
                    change_detected = true;0
                }

                if (window.touched_folders.includes(item_record))
                {
                    base_name_cell.innerHTML +=  "<sup style = 'color: red;'> * </sup>";
                }
            }
            else
            { 
                if (window.the_active_version != 0 && window.active_version_files_data.hasOwnProperty(item_record))
                {
                    var file_commit_state = window.active_version_files_data[item_record]["file_commit_state"];

                    if (file_commit_state != "same")
                    {
                        base_name_cell.innerHTML +=  "<sup style = 'color: blue;'>"+ file_commit_state +"</sup>";
                    }
                }

                if (window.active_version_files_data_tracker.hasOwnProperty(item_record))
                {
                    document.getElementById('is_tracked_' + item_record).checked = true;
                    document.getElementById('is_deployed_' + item_record).checked = window.active_version_files_data_tracker[item_record]["is_deployed"];
                }
                if (setFolderItemMark(item_record) || change_detected)
                {
                    enableElement('action');
                }
            }
        }
    }
}

function asyncPostDashboardFoldersRequest(data)
{
    var the_element = document.getElementById('model_folder');    
    var async_request = new XMLHttpRequest();

    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            the_element.innerHTML = this.responseText;
            
            var the_folder_listener = document.getElementById('dashboard_folder_contents');

            window.current_folder_contents = JSON.parse(the_folder_listener.value);
            setFolderContentMarks();

        }
    }

    the_element.innerHTML = "<div class = 'wait_blinker'>Please wait...</div>";
    async_request.open("POST", '/helpers/folders/dashboard' + "?anti_cache=" + Math.random(), true);
    async_request.send(data);
}

function scanFolder(the_folder, ceiling = "")
{
    var look_level_above = true;

    window.the_folder = the_folder;

    if (the_folder == ceiling)
    {
        look_level_above = false;
    }
    
    var data = {
                        "the_folder": the_folder,
                        "look_level_above": look_level_above
                      };
    var data_json = JSON.stringify(data);
    asyncPostDashboardFoldersRequest(data_json);

    return true;
}

function restoreTrack(absolute_path)
//when restoring the item into active_version_files_data_tracker
//we need the separate entity, not the reference to initial snapshot
//js is heartless bitch
{
    window.active_version_files_data_tracker[absolute_path] = {};

    for (var field in window.active_version_files_data[absolute_path])
    {
        if (window.active_version_files_data[absolute_path].hasOwnProperty(field))
        {
            window.active_version_files_data_tracker[absolute_path][field] = 
            window.active_version_files_data[absolute_path][field];
        }
    }
}

function isTrackedCheckboxChange(absolute_path)
{
    var the_checkbox = document.getElementById("is_tracked_" + absolute_path); 
    var is_deployed_checkbox = document.getElementById("is_deployed_" + absolute_path);

    recordFolderTouch(window.the_folder);

    if (the_checkbox.checked)
    {
        if (window.active_version_files_data.hasOwnProperty(absolute_path) &&
            is_deployed_checkbox.checked != window.active_version_files_data[absolute_path]["is_deployed"])
        {
            is_deployed_checkbox.checked = window.active_version_files_data[absolute_path]["is_deployed"];
            isDeployedCheckboxChange(absolute_path);
        }

        if (!window.active_version_files_data_tracker.hasOwnProperty(absolute_path))
        { //restoring tracking if possible or casting a new if not
            if (window.active_version_files_data.hasOwnProperty(absolute_path))
            {
                restoreTrack(absolute_path);
            }
            else
            {
                window.active_version_files_data_tracker[absolute_path] = window.current_folder_contents[absolute_path];
                window.active_version_files_data_tracker[absolute_path]["file_commit_state"] = "emerged";
                window.active_version_files_data_tracker[absolute_path]["is_deployed"] = false;
                delete window.active_version_files_data_tracker[absolute_path]["is_dir"];
                delete window.active_version_files_data_tracker[absolute_path]["base_name"];
            }
        }
    }
    else
    {
        var track_all_checkbox = document.getElementById("track_all_checkbox");
        if (track_all_checkbox.checked)
        {
            track_all_checkbox.checked = false;
        }

        if (window.active_version_files_data_tracker.hasOwnProperty(absolute_path))
        {
            delete window.active_version_files_data_tracker[absolute_path];
        }
        //and also clear "IsDeployed" checkbox:
        if (is_deployed_checkbox.checked)
        {
            is_deployed_checkbox.checked = false;
            isDeployedCheckboxChange(absolute_path);
        }
    }

    if (setFolderItemMark(absolute_path))
    {
        enableElement('action');
    }
}


function isDeployedCheckboxChange(absolute_path)
{
    var the_checkbox = document.getElementById("is_deployed_" + absolute_path); 

    recordFolderTouch(window.the_folder);

    if (the_checkbox.checked)
    {
        var is_tracked_checkbox = document.getElementById("is_tracked_" + absolute_path);
        if (!is_tracked_checkbox.checked)
        {
            is_tracked_checkbox.checked = true;
            isTrackedCheckboxChange(absolute_path);
        }
    }
    else
    {
        var mark_all_deployable_checkbox = document.getElementById("mark_all_deployable_checkbox");
        if (mark_all_deployable_checkbox.checked)
        {
            mark_all_deployable_checkbox.checked = false;
        }
    }

    if (window.active_version_files_data_tracker.hasOwnProperty(absolute_path))
    {
        window.active_version_files_data_tracker[absolute_path]["is_deployed"] = the_checkbox.checked;
    }

    if (setFolderItemMark(absolute_path))
    {
        enableElement('action');
        enableElement('metadata_button');
    }
}

function onMarkAllDeployableCheckboxChange()
{
   var mark_all_deployable_checkbox = document.getElementById("mark_all_deployable_checkbox");
   
    for (var item in window.current_folder_contents)
    {
        if (window.current_folder_contents.hasOwnProperty(item))
        {
            if (!window.current_folder_contents[item]["is_dir"])
            {
                var is_deployed_checkbox = document.getElementById("is_deployed_" + item);

                if (mark_all_deployable_checkbox.checked != is_deployed_checkbox.checked)
                {
                    is_deployed_checkbox.checked = mark_all_deployable_checkbox.checked;
                    isDeployedCheckboxChange(item);
                }
            }
        }
    }
}

function onTrackAllCheckboxChange()
{
   var track_all_checkbox = document.getElementById("track_all_checkbox");
   
    for (var item in window.current_folder_contents)
    {
        if (window.current_folder_contents.hasOwnProperty(item))
        {
            if (!window.current_folder_contents[item]["is_dir"])
            {
                var is_tracked_checkbox = document.getElementById("is_tracked_" + item);

                if (track_all_checkbox.checked != is_tracked_checkbox.checked)
                {
                    is_tracked_checkbox.checked = track_all_checkbox.checked;
                    isTrackedCheckboxChange(item);
                }
            }
        }
    }
}

function onDashboardLoad()
{
    window.touched_folders = [];
    scanFolder(window.model_path, window.model_path); //model_path defined in the beginning of the Jinja2 block in dashboard.html
}

//=======================================================================
//=======================              ACTIONS             ================================
//=======================================================================
function onSaveDeployDestinationClick()
{
    var new_deploy_destination = popElement("deploy_destination_url").value;
    var confirmation_dialogue_parameters = {};
    var confirmation_message = "<h2> Change <span style = 'color: green;'>"+window.the_model_name+"</span> deploy destination?</h2>\
    <br>\
    <br><b style = 'color: green;'>`"+ window.actual_deploy_destination + 
    "`</b> to `<b style = 'color: red;'>" + new_deploy_destination + "</b>`";
    var helper_url = "/helpers/set_new_deploy_destination";
    var data = 
    {
        "new_deploy_destination": new_deploy_destination,
        "the_model_id": the_model_id
    };
    var data_for_helper = JSON.stringify(data);
    callConfirmationDialogue(confirmation_message, helper_url, data_for_helper);
}

function onSaveMetadataClick()
{

    var data = 
    {
        "metadata_changed": false,
        "actual_metadata": "",
        "deployables_changed": false,
        "changed_items": {}
    };

    data["metadata_changed"] = inputValueHasChanged('active_model_version_metadata', window.actual_metadata);

    if (data["metadata_changed"])
    {
        var actual_metadata = popElement('active_model_version_metadata').value.replace(/'/g, "`");
        data["actual_metadata"] = encodeURI(actual_metadata);
        data["active_version_id"] = window.active_version_id;
    }
    for (var item in window.active_version_files_data)
    {
        if (window.active_version_files_data.hasOwnProperty(item))
        {

            if  (   
                    (window.active_version_files_data_tracker[item])
                    &&
                    (window.active_version_files_data[item]["is_deployed"] != window.active_version_files_data_tracker[item]["is_deployed"])
                )
            {
                data["deployables_changed"] = true;
                var changed_item_id = window.active_version_files_data_tracker[item]["id"];
                data["changed_items"][changed_item_id] = window.active_version_files_data_tracker[item]["is_deployed"];
            }
        }
    }

    if (!data["metadata_changed"] && !data["deployables_changed"])
    {
        alert("No trackable metadata changes, nothing to save.");
        return false;
    }
    
    var data_for_helper = JSON.stringify(data);
    var confirmation_message = "<h2> Update metadata and deployables for <b style = 'color: red;'>v. "+ window.the_active_version + 
    "</b> of <b style = 'color: red;'>"+ window.the_model_name+"</b>?</h2>";
    var helper_url = "/helpers/new_metadata_and_deployables";

    callConfirmationDialogue(confirmation_message, helper_url, data_for_helper);
}

function createNewVersion()
{
    var actual_metadata = popElement('active_model_version_metadata').value.replace(/'/g, "`");
    var passed_files_data = {};
    var deleted_absolute = [];

    for (var folder in active_version_deleted_files)
    {
        if (active_version_deleted_files.hasOwnProperty(folder))
        {
            active_version_deleted_files[folder].forEach
            (
                function(deleted_file)
                {
                    deleted_absolute.push(folder + '/' + deleted_file);        
                }
            );
            
        }
    }

    for (var item in active_version_files_data_tracker)
    {
        if (active_version_files_data_tracker.hasOwnProperty(item))
        {
            if (!deleted_absolute.includes(item))
            {
                passed_files_data[item] = active_version_files_data_tracker[item];
            }
        }
    }

    var data = 
    {
        "model_path": window.model_path,
        "files_tracker": passed_files_data,
        "modified_files": window.active_version_modified_files,
        "model_id": window.the_model_id,
        "new_version_number": parseInt(window.last_version) + 1,
        "the_active_version": window.the_active_version,
        "metadata": encodeURI(actual_metadata)
    }

    var data_for_helper = JSON.stringify(data);
    var helper_url = "/helpers/create_new_version";
    var confirmation_message = "<h2>This will create a new model version. Are all the modifications needed made (e.g. metadata)?</h2>";
    callConfirmationDialogue(confirmation_message, helper_url, data_for_helper);
}

function deleteFile(absolute_path)
{
    var helper_url = "/helpers/delete_file";
    var confirmation_message = "<h2> <span style = 'color:red'>DELETE physically</span> " + absolute_path + "?";
    callConfirmationDialogue(confirmation_message, helper_url, absolute_path);
}

function makeVersionActive(desired_version_id, desired_version_number)
{
    var data = 
    {
        "model_id": window.the_model_id,
        "model_path": window.model_path,
        "desired_version_id": desired_version_id,
        "desired_version_number": desired_version_number
    }

    var data_for_helper = JSON.stringify(data);
    var helper_url = "/helpers/change_active_version";
    var confirmation_message = "<h2>This will physically <span style = 'color:red;'>DELETE</span> the files and subfolders of \
    <span style = 'color:red;'>" + window.the_model_name + 
    "</span> and unpack files of version you choose as active.<br>Files untracked in currently actvie version will be <span style = 'color:red;'>LOST</span>\
    <br><span style = 'color:red;'>PROCEED?</span> </h2>\
    (the db record and archive will remain and possible to activate)<br><br><b style = 'color:red'>" + window.model_path +
    "</b> will be <b style = 'color:red'>purged</b> and refilled with v. " + desired_version_number + " files";

    callConfirmationDialogue(confirmation_message, helper_url, data_for_helper);
}

function restoreFile(absolute_path)
{
    var data = 
    {
        "file_absolute_path": absolute_path,
        "model_path": window.model_path,
        "model_id": window.the_model_id,
        "version_number": window.active_version_number,
        "version_id": window.active_version_id
    }
    var data_for_helper = JSON.stringify(data);

    asyncPostRequestWithRefresh("/helpers/restore_file", data_for_helper);
 }

function deployActiveVersion()
{
    var data = 
    {
        "deploy_url": window.actual_deploy_destination,
        "deploy_id": window.the_model_deploy_id,
        "model_path": window.model_path,
        "model_name": window.the_model_name,
        "model_id": window.the_model_id,
        "version_number": window.active_version_number,
        "files_data": window.active_version_files_data,
        "model_metadata": encodeURI(window.actual_metadata)
    }
    var data_for_helper = JSON.stringify(data);

    var helper_url = "/helpers/deploy";
    var confirmation_message = "<h2>Deploy <span style = 'color: green'> "+ window.the_model_name +
    "</span> v. " + window.active_version_number + "?"

    callConfirmationDialogue(confirmation_message, helper_url, data_for_helper);
 }
