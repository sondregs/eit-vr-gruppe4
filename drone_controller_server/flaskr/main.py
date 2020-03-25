from flask import Blueprint, request

from message.mail.send_email import create_email
from message.message import Message
from ..message_daemon import MessageDaemon


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
