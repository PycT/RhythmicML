#Architecture description

RhythmicML is going to consist of two core parts - client and server parts.

Client and Server are both self-sufficient and independent on each other systems.
When used together Client might receive model's state and data stored from Server by request.

##Client
Client includes UI and is purposed to:
+ Store local configuration
    * deployment destintion
    * models names and metadata
+ Perform local versioning
+ Perform deployment and re-deployment of the model to configured destination
+ Monitor the state of the model in production (optionally)

All the model artifact are stored by Client side in an archive. Archive version contains the whole bunch of files, not changed only.
That is for opportuniti to rollback to any of version and create a new version upon historic one without hustling of what was ever deleted or added and needs to be got rid of.

**Deployment** eventually is sending artifacts via *http[s]*, so the reseiving side might run any ML serving system, maintained to receive.

##Server
Server is a runtime environment with an endpoint to access via http;
It is purposed to:
+ Receive model artiacts and set up serving running and scoring
+ Provide an endpoints to receive production data to score upon and give inferences back
+ Store input and output data with timestamps and trace IDs