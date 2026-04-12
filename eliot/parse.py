"""
Parse a stream of serialized messages into a forest of
``WrittenAction`` and ``WrittenMessage`` objects.
"""

from pyrsistent import PClass, pmap_field, pset_field, discard

from ._message import WrittenMessage, TASK_UUID_FIELD
from ._action import (
    TaskLevel,
    WrittenAction,
    ACTION_STATUS_FIELD,
    STARTED_STATUS,
    ACTION_TYPE_FIELD,
)


class Task(PClass):
    """
    A tree of actions with the same task UUID.
    """

    _nodes = pmap_field(TaskLevel, (WrittenAction, WrittenMessage))
    _completed = pset_field(TaskLevel)
    _root_level = TaskLevel(level=[])

    def root(self):
        """
        @return: The root L{WrittenAction}.
        """
        pass

    def is_complete(self):
        """
        @return bool: True only if all messages in the task tree have been
        added to it.
        """
        pass

    def _insert_action(self, node):
        """
        Add a L{WrittenAction} to the tree.

        Parent actions will be created as necessary.

        @param child: A L{WrittenAction} to add to the tree.

        @return: Updated L{Task}.
        """
        pass

    def _ensure_node_parents(self, child):
        """
        Ensure the node (WrittenAction/WrittenMessage) is referenced by parent
        nodes.

        Parent actions will be created as necessary.

        @param child: A L{WrittenMessage} or L{WrittenAction} which is
            being added to the tree.

        @return: Updated L{Task}.
        """
        pass

    def add(self, message_dict):
        """
        Update the L{Task} with a dictionary containing a serialized Eliot
        message.

        @param message_dict: Dictionary whose task UUID matches this one.

        @return: Updated L{Task}.
        """
        pass


class Parser(PClass):
    """
    Parse serialized Eliot messages into L{Task} instances.

    @ivar _tasks: Map from UUID to corresponding L{Task}.
    """

    _tasks = pmap_field(str, Task)

    def add(self, message_dict):
        """
        Update the L{Parser} with a dictionary containing a serialized Eliot
        message.

        @param message_dict: Dictionary of serialized Eliot message.

        @return: Tuple of (list of completed L{Task} instances, updated
            L{Parser}).
        """
        pass

    def incomplete_tasks(self):
        """
        @return: List of L{Task} that are not yet complete.
        """
        pass

    @classmethod
    def parse_stream(cls, iterable):
        """
        Parse a stream of messages into a stream of L{Task} instances.

        :param iterable: An iterable of serialized Eliot message dictionaries.

        :return: An iterable of parsed L{Task} instances. Remaining
            incomplete L{Task} will be returned when the input stream is
            exhausted.
        """
        pass


__all__ = ["Parser", "Task", "TaskLevel", "WrittenMessage", "WrittenAction"]
