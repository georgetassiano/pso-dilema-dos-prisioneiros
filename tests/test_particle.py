import unittest
import math
import numpy as np
from models.pso.particle import Particle


class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle = Particle()
        self.particle.set_position(np.array([1.0, 1.0]))

    def testUpdatePersonalBest(self):
        best = 0.0
        self.assertEqual(math.inf, self.particle.get_personal_best_value())
        self.assertTrue(np.array_equal(np.array([]), self.particle.get_personal_best_position()))
        self.particle.set_value(best)
        self.assertEqual(best, self.particle.get_personal_best_value())
        self.assertTrue(np.array_equal(np.array([1.0, 1.0]), self.particle.get_personal_best_position()))

    def testUpdateParticle(self):
        global_best_position = np.array([1.0, 1.0])
        inertial = 1.0
        ci = 1.0
        si = 1.0
        self.assertTrue(np.array_equal(np.array([1.0, 1.0]), self.particle.get_position()))
        self.assertTrue(np.array_equal(np.array([]), self.particle.get_velocity()))
        self.particle.update_particle(global_best_position, inertial, ci, si)
        self.assertTrue(np.array_equal(np.array([1.0, 1.0]), self.particle.get_position()))
        self.assertTrue(np.array_equal(np.array([]), self.particle.get_velocity()))


if __name__ == '__main__':
    unittest.main()