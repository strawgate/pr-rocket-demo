"""Simple test runner to execute pytest-style tests without pytest installed.

This runner imports test_*.py modules, resolves fixtures registered via the local
`pytest.fixture` shim, and executes functions named `test_*`. It captures stdout
for tests that use the `capsys` fixture.

It is minimal and tailored to the repository's tests.
"""
import importlib.util
import importlib
import sys
import os
import glob
import inspect
import traceback
from types import SimpleNamespace

# Ensure repo root is on sys.path
ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest as _pytest  # local shim


def load_module_from_path(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def resolve_fixture(name, cache):
    if name in cache:
        return cache[name]
    func = _pytest.get_fixture_function(name)
    if func is None:
        raise KeyError(f"Fixture '{name}' not found")
    sig = inspect.signature(func)
    kwargs = {}
    for p in sig.parameters.values():
        kwargs[p.name] = resolve_fixture(p.name, cache)
    val = func(**kwargs)
    cache[name] = val
    return val


def run_test_function(func, module):
    sig = inspect.signature(func)
    fixture_cache = {}
    args = {}
    # Prepare fixtures for parameters
    for p in sig.parameters.values():
        pname = p.name
        try:
            args[pname] = resolve_fixture(pname, fixture_cache)
        except KeyError:
            args[pname] = None
    # If capsys is provided, redirect stdout while running
    capsys_obj = None
    if 'capsys' in args and args['capsys'] is not None:
        capsys_obj = args['capsys']
    import contextlib, io, sys
    buf = None
    if capsys_obj is not None:
        # redirect stdout/stderr to the capsys writer which delegates to the current buffer
        writer = getattr(capsys_obj, '_writer', None)
        if writer is None:
            writer = capsys_obj._buf
        with contextlib.redirect_stdout(writer):
            try:
                func(**args)
            finally:
                pass
    else:
        # normal execution
        func(**args)


def main():
    tests = sorted(glob.glob(os.path.join(ROOT, "test_*.py")))
    total = 0
    failed = []
    for tpath in tests:
        try:
            mod = load_module_from_path(tpath)
        except Exception:
            print(f"ERROR importing {tpath}")
            traceback.print_exc()
            sys.exit(2)
        # collect test functions
        funcs = [getattr(mod, n) for n in dir(mod) if n.startswith('test_')]
        for f in funcs:
            if not callable(f):
                continue
            total += 1
            try:
                run_test_function(f, mod)
                print(f". {mod.__name__}.{f.__name__}")
            except AssertionError:
                print(f"F {mod.__name__}.{f.__name__}")
                failed.append((mod.__name__, f.__name__, traceback.format_exc()))
            except Exception:
                print(f"E {mod.__name__}.{f.__name__}")
                failed.append((mod.__name__, f.__name__, traceback.format_exc()))
    print("\nRan {} tests".format(total))
    if failed:
        print('\nFailures:')
        for modname, fname, tb in failed:
            print(f"- {modname}.{fname}\n{tb}")
        sys.exit(1)
    print('All tests passed')

if __name__ == '__main__':
    main()
