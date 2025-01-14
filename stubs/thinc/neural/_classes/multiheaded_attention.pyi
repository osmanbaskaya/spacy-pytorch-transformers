# Stubs for thinc.neural._classes.multiheaded_attention (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...api import layerize, with_reshape, wrap
from ..util import get_array_module
from .affine import Affine
from .model import Model
from typing import Any, Optional

def prepare_self_attention(affine: Any, window: Optional[Any] = ..., nM: int = ..., nH: int = ...): ...
def window_mask(n: Any): ...

class MultiHeadedAttention(Model):
    def __init__(self) -> None: ...
    def begin_update(self, Qs_Ks_Vs_masks: Any, drop: float = ...): ...
