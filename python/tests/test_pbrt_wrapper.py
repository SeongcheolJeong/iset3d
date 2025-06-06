import sys
import os
import subprocess
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from python import PBRTWrapper


def test_run_invokes_subprocess():
    wrapper = PBRTWrapper('/path/to/pbrt')
    with mock.patch('subprocess.run') as m_run:
        wrapper.run('scene.pbrt', 'out.exr')
        m_run.assert_called_with([
            '/path/to/pbrt',
            '--outfile',
            'out.exr',
            'scene.pbrt'
        ], check=True)

