from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase
import numpy as np


class DPIndividual10ComBonus(FunctionOptimizationDPIndividualBase):

    def calc_result(self, array, list_arrays = np.array([])):
        """ calcula o resultado da função comparando o array com um outro array aleatório """
        super().calc_result(array, list_arrays)
        value = 0.0
        for i in range(self.get_global_comparison_length()):
            element = np.random.randint(0, np.size(list_arrays, 0))
            for p in range(list_arrays[element].size):
                value += super().get_value(array[p], list_arrays[element][p])
        return value + super().get_bonus(array)
