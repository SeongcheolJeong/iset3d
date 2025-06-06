import os
import sys
from unittest import mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
from python.pbrt_wrapper import PBRTWrapper


def test_run_invokes_subprocess():
    wrapper = PBRTWrapper(pbrt_path="pbrt", verbosity=0)
    with mock.patch("subprocess.run") as run_mock:
        wrapper.run("scene.pbrt", "out.exr")
        run_mock.assert_called()
        args = run_mock.call_args[0][0]
        assert args[0] == "pbrt"
        assert "--outfile" in args
        assert os.path.abspath("out.exr") in args
        assert os.path.abspath("scene.pbrt") in args
