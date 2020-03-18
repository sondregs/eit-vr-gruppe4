from email.message import EmailMessage
from pathlib import Path
from smtplib import SMTP_SSL

from validate_email import validate_email

from ..message import InvalidRecipientError, Message
from ..util import has_connection_to


EMAIL_DIR = Path(__file__).resolve().parent
_FROM_EMAIL = "eit.vr.gruppe4@gmail.com"
_FROM_EMAIL_HOST = "smtp.gmail.com"

CONNECTION_TIMEOUT = 10.0


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
    with SMTP_SSL(_FROM_EMAIL_HOST) as smtp:
        smtp.ehlo()
        smtp.login(_FROM_EMAIL, _FROM_EMAIL_PASSWORD)
        _validate_email(email["To"])
        smtp.send_message(email)


def _validate_email(email_address: str):
    if not validate_email(email_address, verify=True, smtp_timeout=CONNECTION_TIMEOUT):
        # If connection is lost while executing validate_email(), it will return False;
        # therefore, check if that is the case:
        if not has_connection_to(_FROM_EMAIL_HOST, timeout=1.0):
            raise ConnectionError("Lost connection while validating email address.")

        raise InvalidRecipientError(f"Invalid email address: {email_address}")
