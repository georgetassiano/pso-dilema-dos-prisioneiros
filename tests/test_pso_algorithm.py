import unittest
import numpy as np
from models.pso.pso_algorithm import PSOAlgorithm
from models.pso.swarm import Swarm
from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase as DPIndividual
import matplotlib.pyplot as plt

class TestPSOAlgorithm(unittest.TestCase):

    def setUp(self):
        self.particles_length = 50
        self.count_parms = 30
        self.valueIndividual = 1.2 * self.count_parms
        self.valueBonus = self.count_parms * -0.5
        self.array = np.zeros(self.count_parms)
        self.list = np.zeros([50, self.count_parms])
        self.c = 1
        self.bonus = -0.5
        self.lower_limit = 0.0
        self.upper_limit = 1.0
        self.inertial_ini = 1.2
        self.inertial_final = 0.8
        self.ci = 1.0
        self.si = 1.0
        self.function = DPIndividual(self.lower_limit, self.upper_limit)
        self.algorithm = PSOAlgorithm(self.function, 1000, 5)

    def test_exec_algorithm(self):
        self.algorithm.exec_algorithm(self.particles_length, self.function, self.inertial_ini, self.inertial_final, self.ci, self.si)
        result = self.algorithm.get_result()
        result_positions = self.algorithm.get_result_positions()

        best, err_best = self.algorithm.get_best()
        avarage, err_avarage = self.algorithm.get_avarage()
        lowest, err_lowest = self.algorithm.get_lowest()
        entropy = self.algorithm.get_entropy()

        self.assertEqual(5, np.size(result, 0))
        self.assertEqual(1000, np.size(result, 1))
        self.assertEqual(3, np.size(result, 2))
        self.assertEqual(2, np.size(result, 3))

        self.assertEqual(5, np.size(result_positions, 0))
        self.assertEqual(1000, np.size(result_positions, 1))
        self.assertEqual(50, np.size(result_positions, 2))
        self.assertEqual(30, np.size(result_positions, 3))

if __name__ == '__main__':
    unittest.main()
