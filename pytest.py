"""A tiny pytest shim to run tests without external pytest dependency.
Provides a fixture decorator and a few built-in fixtures used by the tests in this repo.
This is intentionally minimal and only supports features used by the test suite here.
"""
import tempfile
from pathlib import Path
import inspect
import types

_fixtures = {}


def fixture(func=None, **kwargs):
    """Decorator to register a fixture by name.
    Usage: @fixture()
    """
    if func is None:
        def decorator(f):
            _fixtures[f.__name__] = f
            return f
        return decorator
    else:
        _fixtures[func.__name__] = func
        return func


def get_fixture_function(name):
    return _fixtures.get(name)


# Built-in fixtures ---------------------------------------------------------
@fixture()
def tmp_path():
    """Return a pathlib.Path to a new temporary directory.
    A fresh directory is created each time the fixture is requested.
    """
    d = tempfile.mkdtemp()
    return Path(d)


@fixture()
def capsys():
    """A simple capture object; test runner will redirect stdout to capture output.
    capsys.readouterr() returns a namespace with 'out' and 'err'.
    """
    class _Capsys:
        def __init__(self):
            import io
            self._buf = io.StringIO()
            # writer delegates to the current buffer so redirect_stdout can remain stable
            class _Writer:
                def __init__(self, parent):
                    self._parent = parent
                def write(self, s):
                    self._parent._buf.write(s)
                def flush(self):
                    try:
                        self._parent._buf.flush()
                    except Exception:
                        pass
            self._writer = _Writer(self)
        def readouterr(self):
            # Return current captured output and reset buffer to mimic pytest behavior
            val = self._buf.getvalue()
            import io
            self._buf = io.StringIO()
            return types.SimpleNamespace(out=val, err='')
    return _Capsys()


# simple mark for compatibility
def mark(*args, **kwargs):
    class _Mark:
        def __init__(self):
            pass
    return _Mark()


# minimal raises context manager to support `with pytest.raises(Error):` in tests
import contextlib

@contextlib.contextmanager
def raises(expected_exception):
    try:
        yield
    except Exception as e:
        if not isinstance(e, expected_exception):
            raise
    else:
        raise AssertionError(f"Did not raise {expected_exception}")


# Expose module-level names used by tests
__all__ = ["fixture", "get_fixture_function", "tmp_path", "capsys", "raises"]
