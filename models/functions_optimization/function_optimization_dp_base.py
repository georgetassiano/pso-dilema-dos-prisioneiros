from models.functions_optimization.function_optimization_base import FunctionOptimizationBase
import numpy as np


class FunctionOptimizationDPBase(FunctionOptimizationBase):

    def __init__(self, min_limit, max_limit, global_comparison_length=1, bonus=0, c=1):
        super().__init__(min_limit, max_limit, True, global_comparison_length)
        self._c = c  # tamanho da cadeia de cooperações
        self._bonus = bonus  # valor do bonus por cadeia de cooperação

    def get_bonus(self, array):
        """ bonus aplicado ao tamanho da cadeia de cooperações em relação a um determinado valor de bonus"""
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

    def generate_array(self):
        return np.random.uniform(self.get_min_limit(), self.get_max_limit(), 30)  # geração de um array de 30 posições definidas aleatoriamente

    def get_max_velocity(self):
        return 0.5
