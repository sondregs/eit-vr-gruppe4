from typing import List

from PIL.ImageFile import ImageFile


class Message:
    def __init__(self, recipient, subject: str, body: str, *, subject_prefix="[Firewatcher]"):
        self.recipient = recipient
        self.subject = f"{subject_prefix} {subject}"
        self.body = body

        self._image_attachments = []

    def add_image_attachment(self, image: ImageFile, image_name: str):
        filename, file_ext = image.filename.rsplit(".", maxsplit=1)
        image_name_parts = image_name.rsplit(".", maxsplit=1)
        if len(image_name_parts) == 2:
            filename, file_ext = image_name_parts
        else:
            filename = image_name

        image.filename = f"{filename}.{file_ext}"
        self._image_attachments.append(image)

    def get_image_attachments(self) -> List[ImageFile]:
        return self._image_attachments

    def __str__(self):
        return "<Message\n" + "\n".join(f"  {k}: '{v}'" for k, v in self.__dict__.items()) + "\n>"


class InvalidRecipientError(Exception):
    pass
