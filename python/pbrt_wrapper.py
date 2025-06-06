"""Local PBRT execution utilities."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class PBRTWrapper:
    """Run PBRT directly without Docker."""

    pbrt_path: str = "pbrt"
    work_dir: Optional[str] = None
    verbosity: int = 1

    def run(
        self, scene_path: str, output_exr: str
    ) -> subprocess.CompletedProcess:
        """Execute PBRT on the local system."""
        scene_path = os.path.abspath(scene_path)
        output_exr = os.path.abspath(output_exr)
        cmd = [self.pbrt_path, "--outfile", output_exr, scene_path]
        if self.verbosity:
            print("Running:", " ".join(cmd))
        return subprocess.run(
            cmd,
            cwd=self.work_dir or os.path.dirname(scene_path),
            capture_output=True,
            text=True,
        )
