import unittest
import numpy as np
from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase as DPIndividual
from models.functions_optimization.function_optimization_dp_coletivo_base import FunctionOptimizationDPColetivoBase as DPColetivo


class TestFunctionOptimization(unittest.TestCase):

    def setUp(self):
        self.count_parms = 30
        self.array = np.zeros(self.count_parms)
        self.list = np.zeros([50, self.count_parms])
        self.c = 1
        self.bonus = np.float_(-0.5)
        self.global_comparison_length_10 = 5
        self.global_comparison_length_30 = 15
        self.value_individual = 1.2 * self.count_parms
        self.value_coletivo = 0 * self.count_parms
        self.value_bonus = self.count_parms * -0.5
        self.lower_limit = 0.0
        self.upper_limit = 1.0

    def test_calc_result_exception(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit)
        with self.assertRaises(ValueError):
            result = function_optimization.calc_result(self.array)

    def test_calc_result_individual_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)

    def test_calc_result_individual_com_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, bonus=self.bonus, c=self.c)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual+self.value_bonus, result)

    def test_calc_result_individual_10_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, global_comparison_length=self.global_comparison_length_10)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)

    def test_calc_result_individual_30_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, global_comparison_length=self.global_comparison_length_30)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)

    def test_calc_result_coletivo_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)

    def test_calc_result_coletivo_com_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, bonus=self.bonus, c=self.c)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual+self.value_bonus, result)

    def test_calc_result_coletivo_10_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, global_comparison_length=self.global_comparison_length_10)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)

    def test_calc_result_coletivo_30_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual(self.lower_limit, self.upper_limit, global_comparison_length=self.global_comparison_length_30)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertAlmostEqual(self.value_individual, result)


if __name__ == '__main__':
    unittest.main()