"""Custom JSON encoding support."""

from typing import Callable
import json
import sys
from pathlib import Path
from datetime import date, time
import platform


class EliotJSONEncoder(json.JSONEncoder):
    """
    DEPRECATED. JSON encoder with additional functionality.

    In particular, supports NumPy types.
    """

    def default(self, o):
        pass


def json_default(o: object) -> object:
    """
    JSON object encoder for non-standard types.  In particular, supports NumPy
    types, Path objects, Pydantic models, dataclasses, Pandas and Polars
    objects.  If you are wrapping it, call it last, as it will raise a
    ``TypeError`` on unsupported types.
    """
    pass


if platform.python_implementation() == "PyPy":
    # We're not using orjson, so need to serialize a few more types.

    original_json_default = json_default

    def json_default(o: object, original_json_default=original_json_default) -> object:
        pass

    json_default.__doc__ = original_json_default.__doc__
    del original_json_default


def _encoder_to_default_function(
    encoder: json.JSONEncoder,
) -> Callable[[object], object]:
    """
    Convert an encoder into a default function usable by ``orjson``.
    """
    pass


try:
    from orjson import dumps as _dumps_bytes

    def _dumps_unicode(o: object, default=None) -> str:
        return _dumps_bytes(o, default=default).decode("utf-8")

except ImportError:

    def _dumps_bytes(o: object, default=None) -> bytes:
        """Serialize an object to JSON, output bytes."""
        return json.dumps(o, default=default).encode("utf-8")

    _dumps_unicode = json.dumps

__all__ = ["EliotJSONEncoder", "json_default"]
