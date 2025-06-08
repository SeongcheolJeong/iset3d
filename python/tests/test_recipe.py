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


def test_synonyms():
    r = Recipe()
    r.set('inputfile', 'scene.pbrt')
    assert r.get('input file') == 'scene.pbrt'
    r.set('outputfile', '/tmp/out.pbrt')
    assert r.get('output dir') == '/tmp'


def test_convenience_methods():
    r = Recipe()
    r.add_light('main', {'type': 'point'})
    assert r.get_light('main')['type'] == 'point'
    r.remove_light('main')
    assert r.get_light('main') is None

    r.add_material('matte', {'kd': [1, 1, 1]})
    assert r.get_material('matte')['kd'] == [1, 1, 1]
    r.remove_material('matte')
    assert r.get_material('matte') is None
