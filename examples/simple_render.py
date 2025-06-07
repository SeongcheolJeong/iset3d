from pathlib import Path

from iset3d import Recipe, PBRTWrapper


def main(output_file='simple_render.exr'):
    """Render the SimpleScene example using PBRTWrapper."""
    # Prepare recipe information
    scene_file = Path('data/scenes/SimpleScene/SimpleScene.pbrt')
    recipe = Recipe.create(name='SimpleScene')
    recipe.set('input file', scene_file)
    recipe.set('output file', output_file)

    # Run PBRT to render the scene
    wrapper = PBRTWrapper('pbrt')
    wrapper.run(str(scene_file), str(output_file))

    recipe.set('rendered file', output_file)
    print(f"Rendered {recipe.get('name')} to {recipe.get('rendered file')}")
    return Path(output_file)


if __name__ == '__main__':
    main()
