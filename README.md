# RhythmicML
A tool for ML models deployment and versioning.

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


by Oct 27th 2019:
 - UI-based Catalogue (models versioning) ready
 - Serving side ready

 Planned:
 - Docker wrapper for serving side
 - Client side CLI Catalogue