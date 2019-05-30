#RhythmicML

This is a tool to deploy ML-models into production in simple and robust fashion, just make it work.

Deployment instanses are designed to be easily assembled into pipelines when multi-stage scoring is presumed.

Each time model deployed, it gets versioned automatically and stored in models storage. All the metadata is stored along.

Deploy might be prepared and performed via CLI tool with configuration defined in dedicated file or via web-UI.

##Definitions

*Model* - an invocable entity making prediction or inference upon an input data. Might be binary artifact produced by ML framework, code, or a combination of both.

*Production Instance* - runtime with a Model wrapped in and API endpoints exposed.

*Deployment* - placing a Model into  a Production Instance


##Preparations for Deployment

Deployment takes a Model itself and a Configuration. 

*Configuration* includes compulsory features, defining Production Instance behaviour, and optional features to accompany Model versioning and management.

Compulsory features include the following:
+ Dependencies: if any dependencies needed to execute a Model loading/scoring - they should be listed line by line in the *requirements.txt* file.
+ Location: an infrastructural unit where a Production Instance is going to run

Optional features:
+ Model description
+ key:value arbitrary metadata

##Workflow

