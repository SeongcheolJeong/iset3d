# Python port (experimental)

This directory contains an early, **experimental** effort to
re-implement portions of the MATLAB based ISET3d toolbox in
Python. The implementation is currently very limited and only
includes a minimal ``Recipe`` data structure and utilities to run
PBRT either through Docker or directly on the local system.

``DockerWrapper`` relies on the local Docker installation and does
not yet support remote execution. Usage::

    from iset3d.python import Recipe, DockerWrapper

    recipe = Recipe(name="ChessSet")
    recipe.set("integrator", {"type": "path"})
    recipe.save("ChessSet.json")

    dw = DockerWrapper()
    dw.run("/path/to/ChessSet.pbrt", "ChessSet.exr")

Alternatively, if you have a local PBRT binary installed you can
use ``PBRTWrapper``::

    from iset3d.python import PBRTWrapper

    pw = PBRTWrapper(pbrt_path="/opt/pbrt/pbrt")
    pw.run("/path/to/ChessSet.pbrt", "ChessSet.exr")

Expect many missing features. Contributions welcome!

