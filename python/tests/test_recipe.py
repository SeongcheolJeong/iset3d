import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from iset3d import Recipe


def test_defaults():
    r = Recipe()
    assert r.name == 'recipe'
    assert r.version == 4
    assert r.materials['list'] == {}
    assert r.media['order'] == []


def test_get_set():
    r = Recipe()
    r.set('input file', 'scene.pbrt')
    assert r.get('input file') == 'scene.pbrt'
    r.set('camera', {'type': 'pinhole'})
    assert r.get('camera')['type'] == 'pinhole'
