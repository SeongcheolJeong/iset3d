from dataclasses import dataclass, field
from typing import Any, Dict


def _normalize(key: str) -> str:
    """Normalize parameter names for comparison."""
    return key.lower().replace(' ', '').replace('_', '')


@dataclass
class Recipe:
    """Container for PBRT recipe data."""

    name: str = 'recipe'
    camera: Any = None
    sampler: Any = None
    film: Any = None
    filter: Any = None
    integrator: Any = None
    renderer: Any = None
    lookAt: Any = None
    scale: Any = None
    world: Any = None
    lights: Any = None
    transformTimes: Any = None

    inputFile: str = ''
    outputFile: str = ''
    renderedFile: str = ''
    version: int = 4

    materials: Dict[str, Any] = field(
        default_factory=lambda: {'list': {}, 'order': [], 'lib': None}
    )
    textures: Any = None
    assets: Any = None
    exporter: str = ''
    media: Dict[str, Any] = field(
        default_factory=lambda: {'list': {}, 'order': [], 'lib': None}
    )
    metadata: Any = None
    recipeVer: int = 2
    hasActiveTransform: bool = False
    verbose: int = 2

    @classmethod
    def create(cls, **kwargs) -> "Recipe":
        """Factory returning a recipe with default values."""
        return cls(**kwargs)

    def _match_attr(self, key: str) -> str:
        norm = _normalize(key)
        for attr in self.__dict__:
            if _normalize(attr) == norm:
                return attr
        raise AttributeError(f"Unknown parameter: {key}")

    def get(self, param: str, default: Any = None) -> Any:
        """Retrieve a parameter value."""
        try:
            attr = self._match_attr(param)
        except AttributeError:
            return default
        return getattr(self, attr)

    def set(self, param: str, value: Any) -> "Recipe":
        """Set a parameter value."""
        attr = self._match_attr(param)
        setattr(self, attr, value)
        return self
