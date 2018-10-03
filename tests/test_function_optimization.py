import unittest
import numpy as np
from models.functions_optimization.dp_individual_sem_bonus import DPIndividualSemBonus
from models.functions_optimization.dp_individual_com_bonus import DPIndividualComBonus
from models.functions_optimization.dp_individual_10_sem_bonus import DPIndividual10SemBonus
from models.functions_optimization.dp_individual_10_com_bonus import DPIndividual10ComBonus
from models.functions_optimization.dp_individual_30_sem_bonus import DPIndividual30SemBonus
from models.functions_optimization.dp_individual_30_com_bonus import DPIndividual30ComBonus
from models.functions_optimization.dp_coletivo_sem_bonus import DPColetivoSemBonus
from models.functions_optimization.dp_coletivo_com_bonus import DPColetivoComBonus
from models.functions_optimization.dp_coletivo_10_sem_bonus import DPColetivo10SemBonus
from models.functions_optimization.dp_coletivo_10_com_bonus import DPColetivo10ComBonus
from models.functions_optimization.dp_coletivo_30_sem_bonus import DPColetivo30SemBonus
from models.functions_optimization.dp_coletivo_30_com_bonus import DPColetivo30ComBonus


class TestFunctionOptimization(unittest.TestCase):

    def setUp(self):
        self.count_parms = 30
        self.valueIndividual = 1.2*self.count_parms
        self.valueColetivo = 0*self.count_parms
        self.valueBonus = (self.count_parms // 3) * -0.5
        self.array = np.zeros(self.count_parms)
        self.list = np.zeros([50, self.count_parms])
        self.c = 3
        self.bonus = -0.5
        self.global_comparison_length = 1
        self.lower_limit = 0.0
        self.upper_limit = 1.0

    def test_calc_result_individual_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividualSemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual, result)

    def test_calc_result_individual_com_bonus_and_result_is_constant(self):
        function_optimization = DPIndividualComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual+self.valueBonus, result)

    def test_calc_result_individual_10_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual10SemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual, result)

    def test_calc_result_individual_10_com_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual10ComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual+self.valueBonus, result)

    def test_calc_result_individual_30_sem_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual30SemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual, result)

    def test_calc_result_individual_30_com_bonus_and_result_is_constant(self):
        function_optimization = DPIndividual30ComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueIndividual+self.valueBonus, result)

    def test_calc_result_coletivo_sem_bonus_and_result_is_constant(self):
        function_optimization = DPColetivoSemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo, result)

    def test_calc_result_coletivo_com_bonus_and_result_is_constant(self):
        function_optimization = DPColetivoComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo+self.valueBonus, result)

    def test_calc_result_coletivo_10_sem_bonus_and_result_is_constant(self):
        function_optimization = DPColetivo10SemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo, result)

    def test_calc_result_coletivo_10_com_bonus_and_result_is_constant(self):
        function_optimization = DPColetivo10ComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo+self.valueBonus, result)

    def test_calc_result_coletivo_30_sem_bonus_and_result_is_constant(self):
        function_optimization = DPColetivo30SemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo, result)

    def test_calc_result_coletivo_30_com_bonus_and_result_is_constant(self):
        function_optimization = DPColetivo30ComBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length, self.c, self.bonus)
        result = function_optimization.calc_result(self.array, self.list)
        self.assertEqual(self.valueColetivo+self.valueBonus, result)


if __name__ == '__main__':
    unittest.main()