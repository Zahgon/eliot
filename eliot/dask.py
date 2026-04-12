"""Support for Eliot tracing with Dask computations."""

from pyrsistent import PClass, field

from dask import compute, optimize, persist

try:
    from dask.distributed import Future
    from dask.highlevelgraph import HighLevelGraph
except:

    class Future(object):
        pass


from dask.core import toposort, get_dependencies, ishashable
from . import start_action, current_action, Action


class _RunWithEliotContext(PClass):
    """
    Run a callable within an Eliot context.

    @ivar task_id: The serialized Eliot task ID.
    @ivar func: The function that Dask wants to run.
    @ivar key: The key in the Dask graph.
    @ivar dependencies: The keys in the Dask graph this depends on.
    """

    task_id = field(type=str)
    func = field()  # callable
    key = field(type=str)
    dependencies = field()

    # Pretend to be underlying callable for purposes of equality; necessary for
    # optimizer to be happy:

    def __eq__(self, other):
        return self.func == other

    def __ne__(self, other):
        return self.func != other

    def __hash__(self):
        return hash(self.func)

    def __call__(self, *args, **kwargs):
        with Action.continue_task(task_id=self.task_id) as action:
            action.log(
                message_type="dask:task", key=self.key, dependencies=self.dependencies
            )
            return self.func(*args, **kwargs)


def compute_with_trace(*args):
    """Do Dask compute(), but with added Eliot tracing.

    Dask is a graph of tasks, but Eliot logs trees.  So we need to emulate a
    graph using a tree.  We do this by making Eliot action for each task, but
    having it list the tasks it depends on.

    We use the following algorithm:

        1. Create a top-level action.

        2. For each entry in the dask graph, create a child with
           serialize_task_id.  Do this in likely order of execution, so that
           if B depends on A the task level of B is higher than the task Ievel
           of A.

        3. Replace each function with a wrapper that uses the corresponding
           task ID (with Action.continue_task), and while it's at it also
           records which other things this function depends on.

    Known issues:

        1. Retries will confuse Eliot.  Probably need different
           distributed-tree mechanism within Eliot to solve that.
    """
    pass


def persist_with_trace(*args):
    """Do Dask persist(), but with added Eliot tracing.

    Known issues:

        1. Retries will confuse Eliot.  Probably need different
           distributed-tree mechanism within Eliot to solve that.
    """
    pass


def _add_logging(dsk, ignore=None):
    """
    Add logging to a Dask graph.

    @param dsk: The Dask graph.

    @return: New Dask graph.
    """
    pass


__all__ = ["compute_with_trace", "persist_with_trace"]
