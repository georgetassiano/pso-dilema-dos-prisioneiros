from models.functions_optimization.function_optimization_base import FunctionOptimizationBase
import numpy as np

class FunctionOptimizationDPColetivoBase(FunctionOptimizationBase):

    def __init__(self, min_limit, max_limit, count_params, global_comparison_length=1, bonus=0, c=1):
        super().__init__(min_limit, max_limit, count_params,  global_comparison_length != 1, global_comparison_length)
        self._c = c
        self._bonus = bonus

    def get_value(self, x, y):
        """ função objetivo """
        if x >= 0.5:
            if y >= 0.5:
                return 30.0
            else:
                return 15.0
        else:
            if y >= 0.5:
                return 15.0
            else:
                return 0.0

    def get_bonus(self, array):
        cop = 0
        count = 0
        for e in array:
            if e < 0.5:
                count += 1
                if count == self._c:
                    cop += 1
                    count = 0
            else:
                count = 0

        return cop * self._bonus

    def calc_result(self, array, list_arrays = np.array([])):
        """ calcula o resultado da função comparando o array com um outro array aleatório """
        super().calc_result(array, list_arrays)
        value = 0.0
        for i in range(self.get_global_comparison_length()):
            element = np.random.randint(0, np.size(list_arrays, 0))
            for p in range(list_arrays[element].size):
                value += self.get_value(array[p], list_arrays[element][p])
        return (value / self.get_global_comparison_length()) + self.get_bonus(array)
