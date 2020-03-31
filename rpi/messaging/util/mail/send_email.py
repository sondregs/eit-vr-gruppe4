import io
import time
from _thread import start_new_thread
from email.message import EmailMessage
from pathlib import Path
from smtplib import SMTP_SSL

from validate_email import validate_email
from wrapt_timeout_decorator import timeout

from util.logging import MESSAGING_LOGGER
from ..message import Message
from ..util import has_connection_to


EMAIL_DIR = Path(__file__).resolve().parent
_FROM_EMAIL = "eit.vr.gruppe4@gmail.com"
_FROM_EMAIL_HOST = "smtp.gmail.com"

EMAIL_TIMEOUT = 15.0


def _get_email_secret():
    email_secret_file = EMAIL_DIR / "email_secret.txt"
    try:
        return email_secret_file.read_text().strip()
    except IOError:
        raise FileNotFoundError(f'Please create the file "{email_secret_file}" containing the password to {_FROM_EMAIL}')


_FROM_EMAIL_PASSWORD = _get_email_secret()

_NUM_VALIDATION_ATTEMPTS = 5
_CONNECTION_TIMEOUT = 3.0


@timeout(EMAIL_TIMEOUT)
def _validate_email(email: str, smtp_timeout: float):
    return validate_email(email, verify=True, smtp_timeout=smtp_timeout)


def check_valid_email(email_address: str):
    def _check_valid_email(address: str):
        def check_connection():
            if not has_connection_to(_FROM_EMAIL_HOST, timeout=_CONNECTION_TIMEOUT):
                raise ConnectionError("Lost connection while validating email address.")

        for attempt in range(1, _NUM_VALIDATION_ATTEMPTS + 1):
            info_message = f'[Attempt #{attempt} validating email address "{address}"]'
            try:
                check_connection()
                if not _validate_email(address, EMAIL_TIMEOUT * 0.9):  # 90% for allowing validate_email() to timeout normally
                    # If connection is lost while executing validate_email(), it will return False;
                    # therefore, check if that is the case:
                    check_connection()
                    MESSAGING_LOGGER.error(f"!!!!! Invalid email address: {address} !!!!!")

                return
            except ConnectionError as e:
                print(f"{info_message} {e}")
                time.sleep(EMAIL_TIMEOUT - _CONNECTION_TIMEOUT)
            except Exception as e:
                print(f"{info_message} {e}")

    start_new_thread(_check_valid_email, (email_address,))


def create_email(message: Message) -> EmailMessage:
    email = EmailMessage()
    email.set_content(message.body)

    email["Subject"] = message.subject
    email["From"] = _FROM_EMAIL
    email["To"] = message.recipient

    for image in message.get_image_attachments():
        image_bytes = io.BytesIO()
        image.save(image_bytes, format=image.format)
        email.add_attachment(image_bytes.getvalue(), maintype='image', subtype=image.format, filename=image.filename)

    return email


@timeout(EMAIL_TIMEOUT)
def send_email(email: EmailMessage):
    with SMTP_SSL(_FROM_EMAIL_HOST) as smtp:
        smtp.ehlo()
        smtp.login(_FROM_EMAIL, _FROM_EMAIL_PASSWORD)
        smtp.send_message(email)
