import numpy as np


class PSOAlgorithm:
    def __init__(self, swarm, function_optimization, max_interation=1, max_execution=1):
        self._max_interation = max_interation
        self._max_execution = max_execution
        self._swarm = swarm
        self._function_optimization = function_optimization
        self._result = np.zeros([max_interation, 3, 2])

    def get_result(self):
        return self._result

    def exec_algorithm(self):
        for e in range(self._max_execution):
            result_execution = np.zeros([self._max_interation, 3, 2])
            for i in range(self._max_interation):
                self._swarm.updateSwarm()
                result_execution[i] = self._swarm.get_information()
            self._result += result_execution
        self._result /= self._max_execution