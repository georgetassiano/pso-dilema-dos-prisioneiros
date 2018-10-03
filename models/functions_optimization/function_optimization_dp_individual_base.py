from models.functions_optimization.function_optimization_base import FunctionOptimizationBase


class FunctionOptimizationDPIndividualBase(FunctionOptimizationBase):

    def __init__(self, min_limit, max_limit, count_params,  global_comparison_length, c=1, bonus=0):
        super().__init__(min_limit, max_limit, count_params,  True, global_comparison_length)
        self._c = c
        self._bonus = bonus

    @staticmethod
    def get_value(x, y):
        """ função objetivo """
        if x >= 0.5:
            if y >= 0.5:
                return 15.0
            else:
                return 0
        else:
            if y >= 0.5:
                return 30.0
            else:
                return 1.2

    def get_bonus(self, array):
        cop = (array < 0.5).sum()
        return (cop // self._c) * self._bonus
