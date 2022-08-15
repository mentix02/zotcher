import sys
import time
import threading
import urllib.parse

from .constants import *


class AsyncSpinner(threading.Thread):
    """
    Used to display a spinner while some other
    job is being processed in the background.
    """

    def __init__(self):
        super().__init__(target=self._spin)
        self._stopevent = threading.Event()

    def stop(self):
        self._stopevent.set()

    def _spin(self):
        while not self._stopevent.is_set():
            for char in "|/-\\":
                sys.stdout.write(f"[{char}]")
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write("\b" * 3)


def valid_url(url: str = DEFAULT_URL) -> str:
    result = urllib.parse.urlparse(url)
    if all([result.scheme, result.netloc]):
        return url


__all__ = ("valid_url", "AsyncSpinner")
