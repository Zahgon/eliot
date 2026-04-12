"""Integration with the standard library ``logging`` package."""

from logging import Handler

from ._action import log_message
from ._traceback import write_traceback


class EliotHandler(Handler):
    """A C{logging.Handler} that routes log messages to Eliot."""

    def emit(self, record):
        pass


__all__ = ["EliotHandler"]
