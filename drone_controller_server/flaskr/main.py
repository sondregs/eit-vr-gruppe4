from flask import Flask, request

from message.mail.send_email import send_email
from message.message import Message

app = Flask(__name__)

to_email = "REPLACE WITH EMAIL ADDRESS"


@app.route("/send_email/")
def send_email_view():
    subject = request.args.get("subject", "")
    body = request.args.get("message", "")
    if subject or body:
        message = Message(to_email, subject, body)
        sent_email = send_email(message)
        sent_email_lines = str(sent_email).splitlines(keepends=False)
        return "<br/>".join(sent_email_lines)
    else:
        return "Subject and/or message have to be set!"
