"""Docker wrapper utilities for PBRT rendering."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class DockerWrapper:
    """Manage local or remote PBRT docker invocations."""

    image: str = "digitalprodev/pbrt-v4-gpu:latest"
    work_dir: Optional[str] = None
    gpu: bool = True
    verbosity: int = 1

    def run(
        self, scene_path: str, output_exr: str
    ) -> subprocess.CompletedProcess:
        """Run PBRT via docker."""
        cmd = [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{os.path.abspath(scene_path)}:/scene:ro",
            self.image,
            "pbrt",
            "--outfile",
            output_exr,
            os.path.basename(scene_path),
        ]
        if self.gpu:
            cmd.insert(2, "--gpus")
            cmd.insert(3, "all")
        if self.verbosity:
            print("Running:", " ".join(cmd))
        return subprocess.run(cmd, capture_output=True, text=True)
