# Deploy

Two general steps of deployment are copying artefacts to serving environment and launching live model instance ready to receive data, score and return predictions.

This API handles uploading model files to the serving infrastructure and automatic settling
parameters to run instance of a *Serving Cell* for particular model. 
 + Create a record of a model in the database
 + Create a folder with unique name for a model received (model id in the database)
 + Put files received to that folder
 + Report deploy_id to Client
 + Start a Serving Cell 

Deployment Server also manages  those Serving Cells:
 + Rise a cell with model loaded and ready to score
    * Start a Cell
    * Ping if it is alive
    * If not - repeat attempt after prolonged interval (few times)
    * Report success/fail to Client

 + Shutdown a Cell on demand
 + Restart a Cell when another version of a model is uploaded.

## Copying artefacts to serving environment

Besides artefacts, which are to be archived into one package and unarchive after transfer,
some descriptive properties are to be reseived by serving side for purposes of unique local naming and server-side tracking and logging.

Apparently there are no way to send data (e.g. JSON) and files with single http-request.
There is a bit of hustle implied if going with handling and integrating on the other side two separate requests for data and file;
Same about encding file into base64 string and sending as data field. Currently I would look at writing necessary data into separate file
ans sending all the files with a single request. 

Only marked as "deployable" files are packed and sent. **Important**: the "deployable" state has to be saved for the active model version (there is a special button for that in UI).

## Preparing and running the scoring instance

There are following common stages possible to highlight in scoring sequence:

+ load an artifact into memory and initialise a handling object (done once per instance launch)
+ receive a data via API request and prepare it for scoring, if neccessary
+ score a data through the model
+ prepare, if necessary, and send the prediction back where API request came from

On a client side a template-based serving script is prepared and uploaded with all the other artifacts.