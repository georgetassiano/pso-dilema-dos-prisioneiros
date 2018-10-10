import unittest
import numpy as np
from models.pso.swarm import Swarm
from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase as DPIndividual


class TestSwarm(unittest.TestCase):

    def setUp(self):
        self.particles_length = 50
        self.count_parms = 30
        self.valueIndividual = 1.2 * self.count_parms
        self.valueColetivo = 0 * self.count_parms
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
        self.iteracao_t = 0
        self.iteracao_final = 1
        self.function = DPIndividual(self.lower_limit, self.upper_limit)
        self.swarm = Swarm(self.particles_length, self.function, self.inertial_ini, self.inertial_final, self.ci, self.si, self.count_parms)

    def testInitSwarm(self):
        self.assertGreaterEqual(self.swarm.get_particles()[-1].get_value(), self.swarm.get_particles()[0].get_value())
        self.assertEqual(self.swarm.get_particles()[0].get_value(), self.swarm.get_global_best_value())
        self.assertTrue(np.array_equal(self.swarm.get_particles()[0].get_position(), self.swarm.get_global_best_particle()))

    def testUpdateSwarm(self):
        global_best_value = self.swarm.get_global_best_value()
        self.swarm.updateSwarm(self.iteracao_t, self.iteracao_final)
        self.assertGreaterEqual(global_best_value, self.swarm.get_global_best_value())

    def testInformationSwarm(self):
        information = self.swarm.get_information()
        self.assertEqual(information[0].sum(), 30)
        self.assertAlmostEqual(information[1].sum(), 30.0)
        self.assertEqual(information[2].sum(), 30)


if __name__ == '__main__':
    unittest.main()