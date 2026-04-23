"""
Custom test runner to execute repository tests without depending on external pytest.

Features implemented to satisfy tests in this repo:
- Discovery of test_*.py files in the repo root
- Importing test modules so they can define fixtures decorated with @pytest.fixture()
- Resolution and invocation of module-level fixtures (including builtin fixtures tmp_path and capsys)
- Capturing stdout/stderr during test execution and exposing it via a capsys fixture with readouterr()
- Support for pytest.raises context manager via the local pytest shim

This runner aims to be small but sufficient for CI verification in this environment.
"""
import importlib.util
import importlib
import inspect
import io
import os
import pkgutil
import pathlib
import sys
import tempfile
import traceback
from types import SimpleNamespace

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def discover_test_files():
    return sorted([p for p in ROOT.glob("test_*.py")])


class Capture:
    def __init__(self):
        self._buf = io.StringIO()

    def write(self, data):
        return self._buf.write(data)

    def flush(self):
        return self._buf.flush()

    def getvalue(self):
        return self._buf.getvalue()

    def clear(self):
        self._buf = io.StringIO()


class Capsys:
    def __init__(self, capture_obj):
        self._capture = capture_obj

    def readouterr(self):
        out = self._capture.getvalue()
        # emulate pytest's behavior: reading empties the buffer
        self._capture.clear()
        return SimpleNamespace(out=out, err="")


# Builtin fixtures provided by this runner
def _builtin_tmp_path(ctx):
    # Create a TemporaryDirectory and store its cleanup object in ctx so the
    # directory isn't removed while tests run.
    d = tempfile.TemporaryDirectory()
    p = pathlib.Path(d.name)
    ctx.setdefault("_tmp_dirs", []).append(d)
    return p


def _builtin_capsys(capture_obj):
    return Capsys(capture_obj)


BUILTIN_FIXTURES = {
    "tmp_path": lambda ctx: _builtin_tmp_path(ctx),
    "capsys": lambda ctx: _builtin_capsys(ctx["capture"]),
}


def import_module_from_path(path: pathlib.Path):
    name = path.stem
    # If already importable, reload to ensure fresh state
    if name in sys.modules:
        return importlib.reload(sys.modules[name])
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def resolve_fixture(name, module, cache, ctx):
    # memoize
    if name in cache:
        return cache[name]

    # Module-level fixture function?
    obj = getattr(module, name, None)
    if callable(obj) and not name.startswith("test"):
        sig = inspect.signature(obj)
        params = []
        for p in sig.parameters.values():
            params.append(resolve_fixture(p.name, module, cache, ctx))
        val = obj(*params)
        cache[name] = val
        return val

    # builtin fixtures
    if name in BUILTIN_FIXTURES:
        val = BUILTIN_FIXTURES[name](ctx)
        cache[name] = val
        return val

    raise RuntimeError(f"Unresolved fixture: {name} in module {module.__name__}")


def run_tests():
    files = discover_test_files()
    if not files:
        print("No tests found")
        return 0

    total = 0
    failures = []

    for f in files:
        mod = import_module_from_path(f)
        funcs = [getattr(mod, n) for n in dir(mod) if n.startswith("test_")]
        for test_func in funcs:
            total += 1
            # fresh fixture cache per-test (function scope fixtures)
            fixture_cache = {}
            # prepare capture
            capture = Capture()
            ctx = {"capture": capture}

            try:
                # Prepare args
                sig = inspect.signature(test_func)
                args = []
                for p in sig.parameters.values():
                    val = resolve_fixture(p.name, mod, fixture_cache, ctx)
                    args.append(val)

                # Redirect stdout/stderr so prints are captured
                old_out, old_err = sys.stdout, sys.stderr
                sys.stdout = capture
                sys.stderr = capture
                try:
                    test_func(*args)
                finally:
                    sys.stdout = old_out
                    sys.stderr = old_err

                print(f". ({mod.__name__}.{test_func.__name__})")
            except Exception as e:
                tb = traceback.format_exc()
                print(f"F ({mod.__name__}.{test_func.__name__})\n{tb}")
                failures.append((mod.__name__, test_func.__name__, tb))

    print("--- Summary ---")
    print(f"Total: {total}, Failures: {len(failures)})")
    if failures:
        for mod, name, tb in failures:
            print(f"Failure in {mod}.{name}:\n{tb}")
        return 1
    return 0


if __name__ == '__main__':
    code = run_tests()
    sys.exit(code)
