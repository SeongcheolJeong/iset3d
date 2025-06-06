"""Utility helpers."""

import os


def pi_root_path() -> str:
    """Return repository root path."""
    return os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
