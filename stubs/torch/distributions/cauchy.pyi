# Stubs for torch.distributions.cauchy (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.distribution import Distribution
from typing import Any, Optional

class Cauchy(Distribution):
    arg_constraints: Any = ...
    support: Any = ...
    has_rsample: bool = ...
    def __init__(self, loc: Any, scale: Any, validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def rsample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...
    def cdf(self, value: Any): ...
    def icdf(self, value: Any): ...
    def entropy(self): ...
