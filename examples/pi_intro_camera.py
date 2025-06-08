from pathlib import Path

from iset3d import Recipe, PBRTWrapper


def main(pinhole_file='camera_pinhole.exr', omni_file='camera_omni.exr'):
    """Approximate the t_piIntro_camera tutorial using PBRTWrapper.

    Two renders are produced: one using a pinhole camera and one using an
    omni camera with a lens file.  The function returns the path to the
    final render (the omni camera image).
    """

    # Create recipe for the SimpleScene example
    scene_file = Path('data/scenes/SimpleScene/SimpleScene.pbrt')
    recipe = Recipe.create(name='SimpleScene')
    recipe.set('input file', scene_file)

    # Configure initial pinhole camera parameters
    recipe.set('output file', pinhole_file)

    # Lights: remove defaults and add a skymap
    for light in ['MoonLight', 'Sky1', 'Sunlight']:
        recipe.remove_light(light)
    recipe.add_light('room_L', {
        'type': 'infinite',
        'mapname': 'room.exr',
        'specscale': 2000
    })

    wrapper = PBRTWrapper('pbrt')

    # First render with pinhole camera
    wrapper.run(str(scene_file), str(pinhole_file))
    recipe.set('rendered file', pinhole_file)
    print(f"Rendered pinhole camera to {pinhole_file}")

    # Switch to omni camera with lens.  Use a lens that exists in the repo
    # so the example runs without requiring additional assets.
    lensfile = 'data/scenes/testplane/dgauss.22deg.3.0mm.json'
    recipe.set('camera', {'type': 'omni', 'lensfile': lensfile})
    recipe.set('output file', omni_file)

    wrapper.run(str(scene_file), str(omni_file))
    recipe.set('rendered file', omni_file)
    print(f"Rendered omni camera using {lensfile} to {omni_file}")
    return Path(omni_file)


if __name__ == '__main__':
    main()
