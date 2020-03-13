import smtplib
from email.message import EmailMessage
from pathlib import Path


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


def send_email(to_email: str, subject: str, message: str, subject_prefix="[Firewatcher]") -> EmailMessage:
    msg = EmailMessage()
    msg.set_content(message)

    msg["Subject"] = f"{subject_prefix} {subject}"
    msg["From"] = _FROM_EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL(_FROM_EMAIL_HOST) as smtp:
        smtp.ehlo()
        smtp.login(_FROM_EMAIL, _FROM_EMAIL_PASSWORD)
        smtp.send_message(msg)

    return msg
