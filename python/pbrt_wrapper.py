import subprocess
from pathlib import Path

class PBRTWrapper:
    """Simple wrapper to run the local PBRT executable."""

    def __init__(self, pbrt_path="pbrt"):
        self.pbrt_path = str(pbrt_path)

    def run(self, scene_file, output_file, extra_args=None, check=True):
        """Run PBRT on a .pbrt scene file and generate an EXR result.

        Parameters
        ----------
        scene_file : str or Path
            Path to the input .pbrt scene description.
        output_file : str or Path
            Destination path for the rendered EXR file.
        extra_args : list, optional
            Additional command line arguments to pass to PBRT.
        check : bool
            If True, ``subprocess.run`` will raise ``CalledProcessError`` on
            failure.
        """
        scene_file = str(scene_file)
        output_file = str(output_file)
        cmd = [self.pbrt_path, "--outfile", output_file]
        if extra_args:
            cmd.extend(extra_args)
        cmd.append(scene_file)
        return subprocess.run(cmd, check=check)
