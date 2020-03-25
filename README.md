# eit-vr-gruppe4
Eksperter i Team - TPG4850 VR landsbyen Gruppe 4 - NTNU

#### Midlertidig oppsett:

##### Installere python pakker:
- `pip install -r requirements.txt`

##### Lokale filendringer:

- Endre mail i `drone_controller_server/flaskr/main.py` til egen mail
- Lage tekstdokument `email_secret.txt i message/mail` med innhold: `96mkTsHDsGPTEjFF`
- Lage tekstdokument controller_server_ip.txt med innhold: `localhost`

##### Starte mail server:
Terminal commands:

1. `export FLASK_APP=drone_controller_server/flaskr/__init__.py`
2. `flask run`

##### Starte å ta bilder
- `python3 run.py`
