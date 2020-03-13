import smtplib
from email.message import EmailMessage
from pathlib import Path

from ..message import Message


EMAIL_DIR = Path(__file__).resolve().parent
_FROM_EMAIL = "eit.vr.gruppe4@gmail.com"
_FROM_EMAIL_HOST = "smtp.gmail.com"


def _get_email_secret():
    email_secret_file = EMAIL_DIR / "email_secret.txt"
    try:
        return email_secret_file.read_text().strip()
    except IOError:
        raise FileNotFoundError(f'Please create the file "{email_secret_file}" containing the password to {_FROM_EMAIL}')


_FROM_EMAIL_PASSWORD = _get_email_secret()


def create_email(message: Message) -> EmailMessage:
    email = EmailMessage()
    email.set_content(message.body)

    email["Subject"] = message.subject
    email["From"] = _FROM_EMAIL
    email["To"] = message.recipient

    return email


def send_email(email: EmailMessage):
    with smtplib.SMTP_SSL(_FROM_EMAIL_HOST) as smtp:
        smtp.ehlo()
        smtp.login(_FROM_EMAIL, _FROM_EMAIL_PASSWORD)
        smtp.send_message(email)
