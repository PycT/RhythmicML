#RhythmicML

This is a tool to deploy ML-models into production in simple and robust fashion, just make it work.

Deployment instanses are designed to be easily assembled into pipelines when multi-stage scoring is presumed.

Each time model deployed, it gets versioned automatically and stored in models storage. All the metadata is stored along.

Deploy might be prepared and performed via CLI tool with configuration defined in dedicated file or via web-UI.

##Functionality

+ Versioning
+ Deployment
+ Monitoring

##Definitions

**Model** - an invocable entity making prediction or inference upon an input data. Might be binary artifact produced by ML framework, code, or a combination of both.

**Production Instance** - runtime with a Model wrapped in and API endpoints exposed.

**Deployment** - placing a Model into  a Production Instance


##Preparations for Deployment

Deployment takes a Model itself and a Configuration. 

**Configuration** includes compulsory features, defining Production Instance behaviour, and optional features to accompany Model versioning and management.

Compulsory features include the following:
+ Dependencies: if any dependencies needed to execute a Model loading/scoring - they should be listed line by line in the *requirements.txt* file.
+ Location: an infrastructural unit where a Production Instance is going to run

Optional features:
+ Model description
+ key:value arbitrary metadata

##Workflow
1. Save a model artifact(s) into a dedicated folder.
2. Configure a model deployment:
    + Dependencies
    + Prediciting script
3. Upload to the scoring infrastructure


##User Interface

UI implementation stack:
* Flask
* SQLite

UI functionality includes:

+ General confguration
    - Default scoring infrastructure location (where to upload a model to)

+ Model configuration
    - scoring infrastructure location, if different from the default one.

+ Model automated versioning

+ Model management
    - model upload 
    - status visualisation
    - productin version switch

##General notes

+ A model is added and deletet vi UI part named `Catalogue` (`catalogue.md`);
+ Model metadata, configurations, versions, commits and deployment are made via UI part named `Dashboard` (`dashboard.md`);
A model version `Dashboard` is entered from `Catalogue`
+ Monitoring is performed via `Monitoring` UI section; Deployed model status is also displayed in `Catalogue` and `Dashboard`