from abc import ABC, abstractmethod
import numpy as np

class FunctionOptimizationBase(ABC):

    def __init__(self, min_limit, max_limit, count_params, global_comparison=False, global_comparison_length=1):
        self._min_limit = min_limit
        self._max_limit = max_limit
        self._count_params = count_params
        self._global_comparison = global_comparison
        self._global_comparison_length = global_comparison_length

    def get_min_limit(self):
        return self._min_limit

    def get_max_limit(self):
        return self._max_limit

    def get_count_params(self):
        return self._count_params

    def get_global_comparison_length(self):
        return self._global_comparison_length

    @abstractmethod
    def calc_result(self, array, list_arrays = np.array([])):
        if self._global_comparison and np.array_equal([], list_arrays):
            raise ValueError("list of arrays is required")
