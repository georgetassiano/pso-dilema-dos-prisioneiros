from abc import ABC, abstractmethod
import numpy as np

class FunctionOptimizationBase(ABC):

    def __init__(self, min_limit, max_limit, global_comparison=False, global_comparison_length=1):
        self._min_limit = min_limit  # limite inferior da função
        self._max_limit = max_limit  # limite superior da função
        self._global_comparison = global_comparison  # verificação se o cálculo da função é realizada individualmente ou em comparação com a população
        self._global_comparison_length = global_comparison_length  # se a comparação for em relação a população, quantos individuos serão comparados

    def get_min_limit(self):
        return self._min_limit

    def get_max_limit(self):
        return self._max_limit

    def get_global_comparison_length(self):
        return self._global_comparison_length

    @abstractmethod
    def calc_result(self, array, list_arrays = np.array([])):
        """ método que define o cálculo da função objetivo da particula """
        if self._global_comparison and np.array_equal([], list_arrays):
            raise ValueError("list of arrays is required")  # verifica se a função objetivo é calculada em relação a comparação da população e então verifica se o array da população foi passado

    @abstractmethod
    def generate_array(self, particle_length):
        """ definição da criação da posição das particulas"""
        pass

    @abstractmethod
    def get_max_velocity(self):
        """ definição da velocidade máxima da atualização das particulas """
        pass
