import unittest
from unittest.mock import MagicMock
import math
import numpy as np
from models.pso.particle import Particle
from models.functions_optimization.function_optimization_dp_coletivo_base import FunctionOptimizationDPColetivoBase


class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle = Particle(np.ones(30))
        self.function_optimization = MagicMock()
        self.function_optimization.get_max_limit = MagicMock(return_value=1.0)
        self.function_optimization.get_min_limit = MagicMock(return_value=0.0)
        self.function_optimization.get_max_velocity = MagicMock(return_value=0.5)

    def test_update_personal_best_to_minimum_global(self):
        """ verifica se a melhor posição da particula é alterada quando a posição atual é melhor """
        best = 0.0
        self.assertEqual(math.inf, self.particle.get_personal_best_value())  # verifica se o valor inicial da melhor posição é infinito
        self.assertTrue(np.array_equal(np.ones(30), self.particle.get_personal_best_position()))  # veirfica se a melhor posição é um array de 1s

        self.particle.set_position(np.zeros(30), self.function_optimization)
        self.particle.set_value(best)

        self.assertEqual(best, self.particle.get_personal_best_value())
        self.assertTrue(np.array_equal(np.zeros(30), self.particle.get_personal_best_position()))

        self.function_optimization.get_min_limit.assert_called_once()
        self.function_optimization.get_max_limit.assert_called_once()

    def test_update_particle(self):
        """ verifica se a particula é alterada quanto a sua velocidade e posição atual """
        global_best_position = np.zeros(30)
        personal_best_position = self.particle.get_personal_best_position()
        inertial = np.float_(1.0)

        self.assertTrue(np.array_equal(personal_best_position, self.particle.get_position())) #verifica se a melhor posição local é igual a posição atual
        self.assertTrue(np.array_equal(np.zeros(30), self.particle.get_velocity())) #verifica se a velocidade está com o valor inicial igual a zero

        self.particle.update_particle(global_best_position, inertial, np.float_(1.0), np.float_(1.0), self.function_optimization)

        self.assertFalse(np.array_equal(personal_best_position, self.particle.get_position())) #verifica se a posição atual foi alterada em relação a melhor posição atual
        self.assertFalse(np.array_equal(np.zeros(30), self.particle.get_velocity())) #verifica se a velocidade atual é diferente de zero
        self.assertLessEqual(self.particle.get_position()[0], 1) # verifica se os valores da posição da particula são menores que o inicial.

        self.function_optimization.get_min_limit.assert_called_once()
        self.function_optimization.get_max_limit.assert_called_once()
        self.function_optimization.get_max_velocity.assert_called()


if __name__ == '__main__':
    unittest.main()