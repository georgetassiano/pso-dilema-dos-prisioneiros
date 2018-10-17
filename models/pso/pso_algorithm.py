import numpy as np
from .swarm import Swarm


class PSOAlgorithm:
    def __init__(self, function_optimization, max_interation=1, max_execution=1):
        self._max_interation = max_interation
        self._max_execution = max_execution
        self._function_optimization = function_optimization
        self._result = np.zeros([max_execution, max_interation, 3, 2])
        self._result_positions = np.array([])

    def get_result(self):
        return self._result

    def get_result_positions(self):
        return self._result_positions

    def get_best(self):
        return np.mean(self._result[:, :, 0, 0], axis=0), np.std(self._result[:, :, 0, 0], axis=0)

    def get_avarage(self):
        return np.mean(self._result[:, :, 1, 0], axis=0), np.std(self._result[:, :, 1, 0], axis=0)

    def get_lowest(self):
        return np.mean(self._result[:, :, 2, 0], axis=0), np.std(self._result[:, :, 2, 0], axis=0)

    def get_entropy(self):
        array_genes = self._result_positions[:, -1, 0, :]
        entropy = np.zeros(self._max_execution)
        for i in range(np.size(self._result, 3)):
            values = [((array_genes[:, i] < 0.5).sum() / self._max_execution), ((array_genes[:, i] >= 0.5).sum() / self._max_execution)]
            entropy_c = 0 if values[0] == 0 else values[0] * np.log2(values[0])
            entropy_e = 0 if values[1] == 0 else values[1] * np.log2(values[1])
            entropy[i] = entropy_c + entropy_e
        return 1 - np.mean(np.absolute(entropy))

    def exec_algorithm(self, number_of_particles, function_optimization, inertial_ini, inertial_final, ci, si):
        result_positions = np.zeros([self._max_execution, self._max_interation, number_of_particles, len(function_optimization.generate_array())])
        for e in range(self._max_execution):
            swarm = Swarm(number_of_particles, function_optimization, inertial_ini, inertial_final, ci, si)
            result_execution = np.zeros([self._max_interation, 3, 2])
            positions_execution = np.zeros([self._max_interation, number_of_particles, len(function_optimization.generate_array())])
            for i in range(self._max_interation):
                swarm.updateSwarm(i, self._max_interation)
                result_execution[i] = swarm.get_information()
                positions_execution[i] = swarm.get_positions()
            self._result[e] = result_execution
            result_positions[e] = positions_execution
        self._result_positions = result_positions
