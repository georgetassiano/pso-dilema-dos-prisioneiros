import unittest
import numpy as np
from models.pso.swarm import Swarm
from models.functions_optimization.dp_individual_sem_bonus import DPIndividualSemBonus


class TestSwarm(unittest.TestCase):

    def setUp(self):
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
        self.swarm = Swarm(50, self.function, self.inertial, self.ci, self.si)

    def testInitSwarm(self):
        self.assertGreaterEqual(self.swarm.get_particles()[-1].get_value(), self.swarm.get_particles()[0].get_value())
        self.assertEquals(self.swarm.get_particles()[0].get_value(), self.swarm.get_global_best_value())
        self.assertTrue(np.array_equal(self.swarm.get_particles()[0].get_position(), self.swarm.get_global_best_particle()))

    def testUpdateSwarm(self):
        global_best_value = self.swarm.get_global_best_value()
        global_best_position = self.swarm.get_global_best_particle()
        self.swarm.updateSwarm()
        self.assertGreaterEqual(global_best_value, self.swarm.get_global_best_value())


if __name__ == '__main__':
    unittest.main()