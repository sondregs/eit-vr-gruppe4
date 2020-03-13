import time
from threading import Thread

from message.mail.send_email import create_email, send_email
from message.message import Message
from rpi_message_client.message_queue import MessageQueue


class MessageDaemon(Thread):
    _WAIT_TIME_BETWEEN_TRIES = 1.0  # seconds

    def __init__(self):
        # Do not set as daemon, as messages need to be finished sent before program terminates
        super().__init__(daemon=False)
        self._message_queue = MessageQueue()

    def run(self):
        while True:
            if self._message_queue.empty():
                self._sleep()
                continue

            try:
                self._send_next_message()
            except ConnectionRefusedError:
                self._sleep()

    def _send_next_message(self):
        def send_func(message: Message):
            email = create_email(message)
            send_email(email)

        self._message_queue.send_next(send_func)

    def add_message_for_sending(self, message: Message):
        self._message_queue.put(message)

    @staticmethod
    def _sleep():
        time.sleep(MessageDaemon._WAIT_TIME_BETWEEN_TRIES)
