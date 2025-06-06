"""Simplified Recipe data structure."""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Recipe:
    """Simplified representation of a PBRT recipe."""

    name: str = "recipe"
    parameters: Dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default=None):
        """Return a parameter value."""
        return self.parameters.get(key, default)

    def set(self, key: str, value):
        """Set a parameter value."""
        self.parameters[key] = value

    def save(self, path: str) -> None:
        """Serialize the recipe to JSON."""
        import json

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {"name": self.name, "parameters": self.parameters}, f, indent=2
            )

    @staticmethod
    def load(path: str) -> "Recipe":
        import json

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        r = Recipe(name=data.get("name", "recipe"))
        r.parameters.update(data.get("parameters", {}))
        return r
