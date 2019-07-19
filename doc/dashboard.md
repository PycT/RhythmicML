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

+ When button [Update version] is pressed all the files tracked are packed as a whole and placed to a storage. Each file gets according record of its status by this version (new/changed/same/deleted)

+ When old version is made current ([ make current ]), all tracked files are deleted and version archive is unpacked.
    A mark of current active version written to a model record. If any changes performed and commited, a new eldest version is created.