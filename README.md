# RhythmicML
A tool for ML models deployment and versioning.

Quick Start:

    Requirements:

    `pip install flask requests rhythmic`

-------------------

    Launch the client-side server (see below), use browser for UI (http://localhost:5000);
    Press "Add model";
    Navigate to the folder with your model and artifacts
    Press "Add"

    A `ModelWrapper.py` class will be copied to that folder - wrap your model and scoring into it. This is compulsory.

    Launch deployment server (see below)

    You are ready to go.

*NOTICE*: a configuration is stored in `configuration.py` file in a `helpers` folder both for client and server side.
-------------------

Client-side preparation:
```
cd ... /src/rhml_client/rhml_client
python setup_db.py
```

Launching UI:

```
cd ... /src/rhml_client/rhml_client
./run.sh
```
or
```
cd ... /src/rhml_client/rhml_client
python -m UI
```

Server-side preparation:
```
cd ... /src/rhml_server/rhml_server
python setup_db.py
```

Launching Server:

```
cd ... /src/rhml_server/rhml_server
./run.sh
```
or
```
cd ... /src/rhml_server/rhml_server
python -m Deploy
```
