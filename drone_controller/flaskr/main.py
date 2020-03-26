from flask import Blueprint, request

from rpi.messaging.daemon.message_daemon import MessageDaemon
from rpi.messaging.util.mail.send_email import create_email
from rpi.messaging.util.message import Message


bp = Blueprint("send_email", __name__, url_prefix="/send_email")

message_daemon = MessageDaemon()
to_email = "REPLACE WITH EMAIL ADDRESS"


def init():
    message_daemon.start()


@bp.route("/", methods=("GET",))
def send_email_view():
    subject = request.args.get("subject", "")
    body = request.args.get("message", "")
    if subject or body:
        message = Message(to_email, subject, body)
        message_daemon.add_message_for_sending(message)

        email = create_email(message)
        email_lines = str(email).splitlines(keepends=False)
        return "--- The following email was added to the sending queue ---<p>" + "<br/>".join(email_lines) + "</p>"
    else:
        return "Subject and/or message have to be set!"
