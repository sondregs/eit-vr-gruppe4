class Message:
    def __init__(self, recipient, subject: str, body: str, *, subject_prefix="[Firewatcher]"):
        self.recipient = recipient
        self.subject = f"{subject_prefix} {subject}"
        self.body = body

        self.attachments = []

    def add_attachments(self, *attachments):
        self.attachments.extend(attachments)

    def __str__(self):
        return "<Message\n" + "\n".join(f"  {k}: '{v}'" for k, v in self.__dict__.items()) + "\n>"


class InvalidRecipientError(Exception):
    pass
