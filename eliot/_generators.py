"""
Support for maintaining an action context across generator suspension.
"""

from sys import exc_info
from functools import wraps
from contextlib import contextmanager
from contextvars import copy_context
from weakref import WeakKeyDictionary

from . import log_message


class _GeneratorContext(object):
    """Generator sub-context for C{_ExecutionContext}."""

    def __init__(self, execution_context):
        self._execution_context = execution_context
        self._contexts = WeakKeyDictionary()
        self._current_generator = None

    def init_stack(self, generator):
        """Create a new stack for the given generator."""
        pass

    @contextmanager
    def in_generator(self, generator):
        """Context manager: set the given generator as the current generator."""
        pass


class GeneratorSupportNotEnabled(Exception):
    """
    An attempt was made to use a decorated generator without first turning on
    the generator context manager.
    """


def eliot_friendly_generator_function(original):
    """
    Decorate a generator function so that the Eliot action context is
    preserved across ``yield`` expressions.
    """
    pass
