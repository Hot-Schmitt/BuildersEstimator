"""
Runs the kit's own test scripts under pytest, so `python3 -m pytest tests/` checks the kit.

The kit's tests are plain scripts that sit beside the code they test (kit/test_*.py) and run on
made-up data only. Each is run here exactly as its own usage line says; a script that fails any
of its checks exits with an error, and that fails the test.
"""
import pathlib
import subprocess
import sys

import pytest

KIT = pathlib.Path(__file__).resolve().parent.parent / "kit"


@pytest.mark.parametrize("script", ["test_estimate_format.py", "test_write_draft.py"])
def test_kit_script(script):
    done = subprocess.run([sys.executable, "-I", str(KIT / script)], capture_output=True, text=True, cwd=KIT)
    assert done.returncode == 0, done.stdout + done.stderr
