import time
from smtplib import SMTPException
from threading import Thread

from .message_queue import MessageQueue
from ..util.mail.send_email import create_email, send_email
from ..util.message import Message


class MessageDaemon(Thread):
    _WAIT_TIME_BETWEEN_TRIES = 3.0  # seconds

    def __init__(self):
        # Do not set as daemon, as messages need to be finished sent before program terminates
        super().__init__(daemon=False)
        self._message_queue = MessageQueue()

    def run(self):
        while True:
            if self._message_queue.empty():
                self._sleep()
                continue

            print("Sending next message...", end="\t\t")
            try:
                self._send_next_message()
            except TimeoutError:
                print("Timed out.")
            except (ConnectionError, SMTPException) as e:
                print(e)
                self._sleep()
            except OSError as e:
                print(e)
                self._sleep()

    def _send_next_message(self):
        def send_func(message: Message):
            email = create_email(message)
            send_email(email)
            print("Message sent!")

        self._message_queue.send_next(send_func)

    def add_message_for_sending(self, message: Message):
        self._message_queue.put(message)

    @staticmethod
    def _sleep():
        time.sleep(MessageDaemon._WAIT_TIME_BETWEEN_TRIES)
