from pathlib import Path

import requests


CURRENT_DIR = Path(__file__).resolve().parent


def _get_webserver_ip() -> str:
    webserver_ip_file = CURRENT_DIR / "controller_server_ip.txt"
    try:
        return webserver_ip_file.read_text().strip()
    except IOError:
        raise FileNotFoundError(f"Please create the file \"{webserver_ip_file.absolute()}\" with the IP address to the drone controller server.")


def send_email(subject: str, message: str):
    webserver_ip = _get_webserver_ip()
    params = {
        "subject": subject,
        "message": message,
    }
    requests.get(f"http://{webserver_ip}:5000/send_email/", params=params)
