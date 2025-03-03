# Stubs for thinc.neural._classes.convolution (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...describe import AttributeDescription, Dimension
from .model import Model
from typing import Any

class ExtractWindow(Model):
    name: str = ...
    nW: Any = ...
    gap: Any = ...
    def __init__(self, nW: int = ..., gap: int = ...) -> None: ...
    def predict(self, X: Any): ...
    def begin_update(self, X__bi: Any, drop: float = ...): ...
