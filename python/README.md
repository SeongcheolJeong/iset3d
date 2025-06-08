# Python utilities for ISET3d

This package provides small helpers for invoking PBRT from Python.

## Using a local PBRT installation

You can render scenes directly with a locally installed PBRT binary without
Docker.  The `PBRTWrapper` class only needs the path to your PBRT executable:

```python
from iset3d import PBRTWrapper

wrapper = PBRTWrapper("/usr/local/bin/pbrt")
wrapper.run("scene.pbrt", "output.exr")
```

## Sample data

The Python package installs a few small scenes so that the examples work
out of the box.  They can be located with ``importlib.resources``:

```python
from importlib import resources
simple = resources.files("iset3d").joinpath("data/scenes/SimpleScene")
``` 

