# Stubs for torch.distributions.distribution (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Distribution:
    has_rsample: bool = ...
    has_enumerate_support: bool = ...
    support: Any = ...
    arg_constraints: Any = ...
    @staticmethod
    def set_default_validate_args(value: Any) -> None: ...
    def __init__(self, batch_shape: Any = ..., event_shape: Any = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...) -> None: ...
    @property
    def batch_shape(self): ...
    @property
    def event_shape(self): ...
    @property
    def arg_constraints(self) -> None: ...
    @property
    def support(self) -> None: ...
    @property
    def mean(self) -> None: ...
    @property
    def variance(self) -> None: ...
    @property
    def stddev(self): ...
    def sample(self, sample_shape: Any = ...): ...
    def rsample(self, sample_shape: Any = ...) -> None: ...
    def sample_n(self, n: Any): ...
    def log_prob(self, value: Any) -> None: ...
    def cdf(self, value: Any) -> None: ...
    def icdf(self, value: Any) -> None: ...
    def enumerate_support(self, expand: bool = ...) -> None: ...
    def entropy(self) -> None: ...
    def perplexity(self): ...
