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

