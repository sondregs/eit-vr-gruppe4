# eit-vr-gruppe4
Eksperter i Team - TPG4850 VR landsbyen Gruppe 4 - NTNU

#### Midlertidig oppsett:

##### Installere python pakker:
- `pip3 install -r requirements.txt`

##### Installere ExifTool
- Installer ExifTool ved å følge instrukser på https://exiftool.org/install.html

##### Lokale filendringer:

- Endre mail i `drone_controller_server/flaskr/main.py` til egen mail
- Lage tekstdokument `email_secret.txt` i `message/mail` med 16-tegns kode i slack
- Lage tekstdokument `controller_server_ip.txt` i `rpi_client_message` med innhold: `localhost`

##### Starte mail server:
Terminal commands:

I `eit-vr-gruppe4` mappen
1. `export FLASK_APP=drone_controller_server/flaskr/__init__.py`
2. `flask run`

##### Starte å ta bilder
I `eit-vr-gruppe4` mappen
- `python3 run.py`
