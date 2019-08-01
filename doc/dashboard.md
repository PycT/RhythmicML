#Dashboard

The dashboard of a models is an interface section, where a model's properties are displayed and
parameters are configured.

Version is updated here either.


##Displayed properties:

+ Model Name
+ Model Path
+ Current Active Version/ Last Version
+ Deploy Destination URL
    * this URL might be checked via button [check]: request is sent, response status displayed along with timestamp.
+ Description
+ Versions list

For each version:

+ Metadata text
+ Commit comment

+ Tracked files list
    * Each item accompanied with a check box, if checked - file is tracked.
    * If the file is tracked, than it's change time is checked - if later than recorded to version - it is marked as changed.
    * If the list is changed - an "update version" button is available

+ [ make this version current ] button
+ [ delete version ] button


##Workflows

+ All the model version are displayed as a list. All the static data - properties, files list - are folded under according version list item.
The Active Version (the version user works with currently, it is not neccessarily the last version) is displayed unfolded.

+ Model version static data incudes metadat field with arbitrary text data and tracked files list. Besides flag of being tracked, file might have flag of being deployable. That means that file is copied to deploy destination and used in ML production along with the model (or it is the model itself).

+ The files are tracked relatively to the active modelversion only. State of being changed is tracked via the file's last change timestamp system property.

+ Static data update and new version creation are accessible for the active modelversion only.

+ Actions with active version static data (buttons):
    * Update metadata for v. {{active_version_number}} - rewrites metadata for current version.
    * Save all changes to v. {{last_version_number + 1}} - creates a new version.
        This button is rendered for the active version only. By default it is disabled. It gets enabled when the metadata changes or any changes in tracked files detected.
    * Discard unsaved changes - reloads the page.

+ Actions with non-active modelversions:
    * Make active - removes all tracked files of currently active modelversion and unpacks the selected one.

+ **All the actions are made with compulsory explicit confirmation!!!**

+ When a new modelversion created, all the files tracked are packed as a whole and placed to a storage. Each file gets according record of its status by this version (new/changed/same/deleted)

+ When older version is made current, all tracked files are deleted and version archive is unpacked.
    A mark of current active version written to a model record. If any changes performed and commited, a new eldest version is created.