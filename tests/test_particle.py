import unittest
import math
import numpy as np
from models.pso.particle import Particle


class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle = Particle(0.0, 1.0, 30)

    def test_update_personal_best_to_Mminimum_global(self):
        """ verifica se a melhor posição da particula é alterada quando a posição atual é melhor """
        best = 0.0
        personal_best_position = self.particle.get_personal_best_position()

        self.assertEqual(math.inf, self.particle.get_personal_best_value())
        self.assertTrue(np.array_equal(personal_best_position, self.particle.get_personal_best_position()))

        self.particle.set_position(np.zeros(30))
        self.particle.set_value(best)

        self.assertEqual(best, self.particle.get_personal_best_value())
        self.assertFalse(np.array_equal(personal_best_position, self.particle.get_personal_best_position()))
        self.assertTrue(np.array_equal(np.zeros(30), self.particle.get_personal_best_position()))

    def test_update_particle(self):
        """ verifica se a particula é alterada quanto a sua velocidade e posição atual """
        global_best_position = np.zeros(30)
        personal_best_position = self.particle.get_personal_best_position()
        inertial = np.float_(1.0)

        self.assertTrue(np.array_equal(personal_best_position, self.particle.get_position())) #verifica se a melhor posição local é igual a posição atual
        self.assertTrue(np.array_equal(np.zeros(30), self.particle.get_velocity())) #verifica se a velocidade está com o valor inicial igual a zero

        self.particle.update_particle(global_best_position, inertial, np.float_(1.0), np.float_(1.0))

        self.assertFalse(np.array_equal(personal_best_position, self.particle.get_position())) #verifica se a posição atual foi alterada em relação a melhor posição atual
        self.assertFalse(np.array_equal(np.zeros(30), self.particle.get_velocity())) #verifica se a velocidade atual é diferente de zero


if __name__ == '__main__':
    unittest.main()