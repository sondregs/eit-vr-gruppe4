# eit-vr-gruppe4
Prosjektet til gruppe 4 i TPG4850 - VR-landsbyen ved NTNU.


#### Midlertidig oppsett:

##### Installere python pakker:
- `pip3 install -r requirements.txt`

##### Installere ExifTool
- Installer ExifTool ved å følge instrukser på https://exiftool.org/install.html

##### Oppsett lokalt:
- Endre `to_email` i [`rpi/messaging/sending.py`](/rpi/messaging/sending.py) til ønsket e-postadresse
- Lag tekstfila `email_secret.txt` i [`rpi/messaging/util/mail`](/rpi/messaging/util/mail) med passordet til eit.vr.gruppe4@gmail.com (står på Slack)

##### Starte å ta bilder og sende varsler
Fra øverste mappen i repoet:
- `python3 run.py`
