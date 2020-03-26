from typing import Tuple

from PIL.ImageFile import ImageFile

from .daemon.message_daemon import MessageDaemon
from .util.message import Message


message_daemon = MessageDaemon()
# TODO: find fitting permanent email
to_email = "REPLACE WITH EMAIL ADDRESS"


def init():
    message_daemon.start()


def send_alert(subject: str, message: str, *image_imagename_tuples: Tuple[ImageFile, str]):
    message_obj = Message(to_email, subject, message)
    for image, image_name in image_imagename_tuples:
        message_obj.add_image_attachment(image, image_name)

    message_daemon.add_message_for_sending(message_obj)
