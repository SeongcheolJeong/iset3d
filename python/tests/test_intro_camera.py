import os
import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from examples import pi_intro_camera
from iset3d import PBRTWrapper


def test_pi_intro_camera_creates_output(tmp_path):
    pinhole = tmp_path / 'pinhole.exr'
    omni = tmp_path / 'omni.exr'

    def fake_run(self, scene_file, out_file, extra_args=None, check=True):
        Path(out_file).write_text('dummy')
        return mock.MagicMock()

    with mock.patch.object(PBRTWrapper, 'run', new=fake_run):
        result = pi_intro_camera.main(pinhole_file=str(pinhole), omni_file=str(omni))
        assert result.exists()
