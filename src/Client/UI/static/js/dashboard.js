"use strict";

//toggleDisplay(), setVisible(), setInvisible(), popElement(), enableElement(), inputValueHasChanged()
// elementIsDisabled()
// and other manipulations with DOM are defied in manipulations.js
//
//asyncPostRequest(), asyncPostRequestWithRefresh() are defined in async_requests.js

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
    folder_item.style.color = "#00cc00";
}

function resetFileMark(absolute_path)
{
    var folder_item = document.getElementById("folder_item_"+absolute_path);
    folder_item.style.fontWeight = "";
    folder_item.style.backgroundColor = "";
    folder_item.style.color = "";
}

function setFolderContentMarks()
//color changes and set checkboxes in accordance with db records
//------
//window.current_folder_contents - scanned folder contents
//window.active_version_files_data - db snapshot
//window.active_version_files_data_tracker - to track user made changes
//------
//<button id = "action" disabled>Save All as v. {{model_static_data["properties"]["last_version"] + 1}}</button> -
// - activate it if any changes detected
{
    for (var item_record in window.current_folder_contents)
    {
        if ( window.current_folder_contents.hasOwnProperty(item_record) && 
            !window.current_folder_contents[item_record]["is_dir"])
        //we are looking onto files here
        {
            var item = window.current_folder_contents[item_record];
            var change_detected = false;

            if (window.active_version_files_data_tracker.hasOwnProperty(item_record))
            //if the file is tracked
            {
                document.getElementById("is_tracked_" + item_record).checked = true;
                //show it in UI

                if (!window.active_version_files_data.hasOwnProperty(item_record))
                //if the file was not tracked when the version was created - change happened
                {
                    change_detected = true;
                }
                else
                //if it was - let us check system 'last modfied' file attribute
                {
                    if (item["last_modified_time"] != window.active_version_files_data_tracker[item_record]["last_modified_time"])
                    {
                        change_detected = true;
                    }
                }

                if (window.active_version_files_data_tracker[item_record]["is_deployed"])
                //if the file is marked as deployable - shiw it in UI   
                {
                    document.getElementById("is_deployed_" + item_record).checked = true;

                    if (!window.active_version_files_data[item_record]["is_deployed"])
                    //was it marked as deployable when the version was created?
                    {
                        change_detected = true;
                    }
                }
            }
            else
            //if the file is not tracked
            {
                if (window.active_version_files_data.hasOwnProperty(item_record))
                //was it tracked when the version was created?
                {
                    change_detected = true;
                }
                else
                //if not - it is a new file to the active version
                {
                    markNewFile(item_record);
                }
            }

            if (change_detected)
            {
                markFileChange(item_record);
                enableElement('action');
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

function isTrackedChange(absolute_path)
{
    the_checkbox = popElement("is_tracked_" + item_record); 

    if (the_checkbox.checked)
    {

    }
}