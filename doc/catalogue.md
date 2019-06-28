#Catalogue - index.html

The dashboard is a list of all the models tracked by the system [RhythmicML]

##Functions:

+ Add a model to the tracking list
+ Delete a model from the tracking list
+ Display the tracking list


##UI elements:

+ Button "Add".
+ "Search" field to search a model.
    The Search input acts as a filter for the tracking list - only models with containing an input names stay in the list, with that part of the name highlighted.
+ Tracking list.
+ List is ordered descending by the timestamp of last changes.
+ Each list-item contains an element, unfolding sublist of the model's versions.
+ Each list item has UI-element to delete model from the list.
+ Each list item has a UI element to rename the model.

Model names and model versions in sublist are clickable, leading to the dashboard.
Click on the model's name leads to the dashboard of the last version of the model.
Dashboards of all the versions except the last one are read-only.

##Tracking list

Enumerated list of tracked model.

**Each list item** displays:
+ Model name
+ Last version number
+ Path to the folder, containing the model
+ Timestamp of the last change commit
+ [?] Status if changed compared to the last commit
+ Each list item has UI-element to delete model from the list.
+ Each list item has a UI element to rename the model.

##Workflow

###Adding a model to the tracking list
To add a model to the tracker, User presses **the "Add" button** on the dashboard. A dialogue appears to select a folder, containing a model with all the accompanying files to track. The model inititally named after the containing folder. If there is already a model with such a name in hte base, a number **1** is added to the name, then checked again. This repeats with increasing the number until the unique name is figured. 

0. The path is checked to be already present in the database. If true, the according status returned, workflow stops.
1. The record containing model name, model path and the timestamp is added to `models_table`.
2. The record of version 0 is added to `versions_table`.
3. The model folder is scanned recursiveliy, adding all the files found to the `files_table` (absolute paths). 
4. The `.rhml_storage` folder created within specified model directory.
5. The initial, 0-version archive is created.

###Managing the model files tracking and versions: see the `dashboard.md`

###Deleting a model from tracking list
When User wishes to delete a model, he is prompted to input model's name to confirm deleteion. The deletion is irreversible.

After confirmation `models_table`, `versions_table` and `files_table` are cleaned accordingly.

Cleaning Server side is up to User.
