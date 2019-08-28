# RhythmicML Server

Server side presumes carrying functions of ML models deployment and serving.

Deployment and Serving are two separate APIs.

## Deployment

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

## Serving

Each model is scored in an individual environment, which is basically a Flask-application we will call here "Serving Cell".

Common methods of a Serving Cell:

+ accept and decode an input data
+ score the model upon that data
+ encode and send back a prediction made 
+ answer a ping for living-sign (check if a Cell is alive)
+ handle endpoints for external monitoring needs:
    provide and expose unique trace id for each input received and prediction upon that input

 # Important notes
 Cells interact with custom user's applications independently on Deployment Server.