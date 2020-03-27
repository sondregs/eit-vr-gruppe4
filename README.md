# eit-vr-gruppe4
Eksperter i Team - TPG4850 VR landsbyen Gruppe 4 - NTNU

#### Midlertidig oppsett:

##### Installere python pakker:
- `pip3 install -r requirements.txt`

##### Installere ExifTool
- Installer ExifTool ved å følge instrukser på https://exiftool.org/install.html
- Kontroler at ExifTool er lagt til i PATH ved å skrive inn `exiftool` i komandolinjen

##### Lokale filendringer:

- Endre mail i `rpi/messaging/sending.py` til egen mail
- Lage tekstdokument `email_secret.txt` i `rpi/messaging/util/mail` med 16-tegns kode i slack
- Lage tekstdokument `controller_server_ip.txt` i `rpi_client_message` med innhold: `localhost`

##### Starte mail server:
Terminal commands:

I `eit-vr-gruppe4` mappen
1. `export FLASK_APP=drone_controller/flaskr/__init__.py`
2. `flask run`

##### Starte å ta bilder
I `eit-vr-gruppe4` mappen
- `python3 run.py`
