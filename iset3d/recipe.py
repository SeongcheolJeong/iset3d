from dataclasses import dataclass, field
from typing import Any, Dict
from pathlib import Path


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
    lights: Dict[str, Any] = field(default_factory=dict)
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

    # Mappings for commonly used aliases in get/set
    _GET_ALIASES = {
        'inputbasename': lambda self: Path(self.inputFile).stem,
        'inputdir': lambda self: str(Path(self.inputFile).parent),
        'outputbasename': lambda self: Path(self.outputFile).stem,
        'outputdir': lambda self: str(Path(self.outputFile).parent),
    }

    _SET_ALIASES = {
        'inputfile': 'inputFile',
        'outputfile': 'outputFile',
        'renderedfile': 'renderedFile',
        'lookat': 'lookAt',
    }

    @classmethod
    def create(cls, **kwargs) -> "Recipe":
        """Factory returning a recipe with default values."""
        return cls(**kwargs)

    def _match_attr(self, key: str) -> str:
        norm = _normalize(key)
        alias = self._SET_ALIASES.get(norm)
        if isinstance(alias, str):
            return alias
        for attr in self.__dict__:
            if _normalize(attr) == norm:
                return attr
        raise AttributeError(f"Unknown parameter: {key}")

    def get(self, param: str, default: Any = None) -> Any:
        """Retrieve a parameter value."""
        norm = _normalize(param)
        if norm in self._GET_ALIASES:
            func = self._GET_ALIASES[norm]
            return func(self)
        try:
            attr = self._match_attr(param)
        except AttributeError:
            return default
        return getattr(self, attr)

    def set(self, param: str, value: Any) -> "Recipe":
        """Set a parameter value."""
        norm = _normalize(param)
        if norm in self._SET_ALIASES:
            param = self._SET_ALIASES[norm]
        attr = self._match_attr(param)
        setattr(self, attr, value)
        return self

    # Convenience methods for lights and materials
    def add_light(self, name: str, data: Any) -> "Recipe":
        self.lights[name] = data
        return self

    def remove_light(self, name: str) -> "Recipe":
        self.lights.pop(name, None)
        return self

    def get_light(self, name: str, default: Any = None) -> Any:
        return self.lights.get(name, default)

    def add_material(self, name: str, data: Any) -> "Recipe":
        self.materials['list'][name] = data
        if name not in self.materials['order']:
            self.materials['order'].append(name)
        return self

    def remove_material(self, name: str) -> "Recipe":
        self.materials['list'].pop(name, None)
        if name in self.materials['order']:
            self.materials['order'].remove(name)
        return self

    def get_material(self, name: str, default: Any = None) -> Any:
        return self.materials['list'].get(name, default)
