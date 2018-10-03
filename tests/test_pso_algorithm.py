import unittest
import numpy as np
from models.pso.pso_algorithm import PSOAlgorithm
from models.pso.swarm import Swarm
from models.functions_optimization.dp_individual_sem_bonus import DPIndividualSemBonus


class TestPSOAlgorithm(unittest.TestCase):

    def setUp(self):
        self.particles_length = 50
        self.count_parms = 30
        self.valueIndividual = 1.2 * self.count_parms
        self.valueColetivo = 0 * self.count_parms
        self.valueBonus = (self.count_parms // 3) * -0.5
        self.array = np.zeros(self.count_parms)
        self.list = np.zeros([50, self.count_parms])
        self.c = 3
        self.bonus = -0.5
        self.global_comparison_length = 1
        self.lower_limit = 0.0
        self.upper_limit = 1.0
        self.inertial = 1.0
        self.ci = 1.0
        self.si = 1.0
        self.function = DPIndividualSemBonus(self.lower_limit, self.upper_limit, self.count_parms, self.global_comparison_length)
        self.swarm = Swarm(self.particles_length, self.function, self.inertial, self.ci, self.si)
        self.algorithm = PSOAlgorithm(self.swarm, self.function, 1000)

    def test_exec_algorithm(self):
        self.algorithm.exec_algorithm()
        result = self.algorithm.get_result()
        self.assertEqual(1000, np.size(result, 0))
        self.assertEqual(3, np.size(result, 1))
        self.assertEqual(2, np.size(result, 2))


if __name__ == '__main__':
    unittest.main()
