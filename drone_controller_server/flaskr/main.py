from flask import Flask, request

from mail.send_email import send_email

app = Flask(__name__)

to_email = "REPLACE WITH EMAIL ADDRESS"


@app.route("/send_email/")
def send_email_view():
    subject = request.args.get("subject", "")
    message = request.args.get("message", "")
    if subject or message:
        sent_email = send_email(to_email, subject, message)
        sent_email_lines = str(sent_email).splitlines(keepends=False)
        return "<br/>".join(sent_email_lines)
    else:
        return "Subject and/or message have to be set!"
