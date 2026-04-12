"""
API and command-line support for human-readable Eliot messages.
"""

import pprint
import argparse
from datetime import datetime
from sys import stdin, stdout
from collections import OrderedDict
from json import dumps

from json import loads

from ._message import (
    TIMESTAMP_FIELD,
    TASK_UUID_FIELD,
    TASK_LEVEL_FIELD,
    MESSAGE_TYPE_FIELD,
)
from ._action import ACTION_TYPE_FIELD, ACTION_STATUS_FIELD


# Ensure binary stdin, since we expect specifically UTF-8 encoded
# messages, not platform-encoding messages.
stdin = stdin.buffer


# Fields that all Eliot messages are expected to have:
REQUIRED_FIELDS = {TASK_LEVEL_FIELD, TASK_UUID_FIELD, TIMESTAMP_FIELD}

# Fields that get treated specially when formatting.
_skip_fields = {
    TIMESTAMP_FIELD,
    TASK_UUID_FIELD,
    TASK_LEVEL_FIELD,
    MESSAGE_TYPE_FIELD,
    ACTION_TYPE_FIELD,
    ACTION_STATUS_FIELD,
}

# First fields to render:
_first_fields = [ACTION_TYPE_FIELD, MESSAGE_TYPE_FIELD, ACTION_STATUS_FIELD]


def _render_timestamp(message: dict, local_timezone: bool) -> str:
    """Convert a message's timestamp to a string."""
    pass


def pretty_format(message: dict, local_timezone: bool = False) -> str:
    """
    Convert a message dictionary into a human-readable string.

    @param message: Message to parse, as dictionary.

    @return: Unicode string.
    """
    pass


def compact_format(message: dict, local_timezone: bool = False) -> str:
    """Format an Eliot message into a single line.

    The message is presumed to be JSON-serializable.
    """
    pass


_CLI_HELP = """\
Convert Eliot messages into more readable format.

Reads JSON lines from stdin, write out pretty-printed results on stdout.
"""


def _main():
    """
    Command-line program that reads in JSON from stdin and writes out
    pretty-printed messages to stdout.
    """
    pass


__all__ = ["pretty_format", "compact_format"]
