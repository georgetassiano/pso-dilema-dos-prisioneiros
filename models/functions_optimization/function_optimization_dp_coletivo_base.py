from models.functions_optimization.function_optimization_dp_base import FunctionOptimizationDPBase
import numpy as np

class FunctionOptimizationDPColetivoBase(FunctionOptimizationDPBase):

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

    def calc_result(self, array, list_arrays = np.array([])):
        """ calcula o resultado da função comparando o array com um outro array aleatório """
        super().calc_result(array, list_arrays)
        value = 0.0
        for i in range(self.get_global_comparison_length()):
            element = np.random.randint(0, np.size(list_arrays, 0))
            for p in range(list_arrays[element].size):
                value += self.get_value(array[p], list_arrays[element][p])
        return (value / self.get_global_comparison_length()) + self.get_bonus(array)


