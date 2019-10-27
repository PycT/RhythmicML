# RhythmicML
A tool for ML models deployment and versioning.

Client-side preparation:
```
cd ... /src/Client
python setup_db.py
```

Launching UI:

```
cd ... /src/Client
./run.sh
```
or
```
cd ... /src/Client
python -m UI
```

Server-side preparation:
```
cd ... /src/Server
python setup_db.py
```

Launching Server:

```
cd ... /src/Server
./run.sh
```
or
```
cd ... /src/Server
python -m Deploy
```


by Oct 27th 2019:
 - UI-based Catalogue (models versioning) ready
 - Serving side ready

 Planned:
 - Docker wrapper for serving side
 - Client side CLI Catalogue