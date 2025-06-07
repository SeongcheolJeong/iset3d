import os
import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from examples import simple_render
from iset3d import PBRTWrapper


def test_simple_render_creates_output(tmp_path):
    output = tmp_path / 'result.exr'

    def fake_run(self, scene_file, out_file, extra_args=None, check=True):
        Path(out_file).write_text('dummy')
        return mock.MagicMock()

    with mock.patch.object(PBRTWrapper, 'run', new=fake_run):
        result_path = simple_render.main(output_file=str(output))
        assert result_path.exists()
