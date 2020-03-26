from collections import deque
from typing import Any, Callable

from ..util.message import InvalidRecipientError, Message


class MessageQueue:
    def __init__(self):
        self._queue = deque()

    def empty(self):
        return len(self._queue) == 0

    def put(self, message: Message):
        self._queue.append(message)

    def send_next(self, send_func: Callable[[Message], Any]):
        if self.empty():
            raise IndexError("Can't send message when queue is empty.")

        head_index = 0
        try:
            send_func(self._queue[head_index])
        except InvalidRecipientError:
            # Remove message if invalid recipient
            invalid_message = self._queue.popleft()
            print("Invalid recipient:")
            print(invalid_message)
            return

        self._queue.popleft()

    def __str__(self):
        return str(self._queue)
