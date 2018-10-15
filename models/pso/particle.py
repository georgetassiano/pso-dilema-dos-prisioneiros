import numpy as np


class Particle:
    def __init__(self, position):
        self._position = position  # posição atual da particula
        self._value = np.inf  # valor atual da particula
        self._velocity = np.zeros(len(position))  # velocidade atual da particula
        self._personal_best_position = self._position.copy()  # melhor posição da particula
        self._personal_best_value = np.inf  # melhor valor da particula

    def __eq__(self, other):
        return self._value == other.get_value()

    def __lt__(self, other):
        return self._value < other.get_value()

    def get_position(self):
        return self._position

    def set_position(self, position, function_optimization):
        self._position = np.clip(position, function_optimization.get_min_limit(), function_optimization.get_max_limit())  # espelhando valores menores ou maiores que a função permite para o minimo e máximo.

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.update_personal_best()

    def set_velocity(self, value, function_optimization):
        self._velocity = np.clip(value, -function_optimization.get_max_velocity(), function_optimization.get_max_velocity())  # define a velocidade máxima que a particula pode se movimentar

    def get_velocity(self):
        return self._velocity

    def get_personal_best_position(self):
        return self._personal_best_position

    def get_personal_best_value(self):
        return self._personal_best_value

    def get_personal_best_information(self):
        """ retorna o número de cooperações e delações, respectivamente, melhores obtidos da particula """
        return np.array([(self._personal_best_position < 0.5).sum(), (self._personal_best_position >= 0.5).sum()])

    def get_position_information(self):
        """ retorna o número de cooperações e delações, respectivamente, atuais da particula """
        return np.array([(self._position < 0.5).sum(), (self._position >= 0.5).sum()])

    def update_personal_best(self):
        """ se a posição atual for melhor que a melhor posição da particula, então deve receber a nova posição """
        if self._value <= self._personal_best_value:
            self._personal_best_value = self._value
            self._personal_best_position = self._position

    def update_particle(self, global_best_particle, inertial, ci, si, function_optimization):
        """ Deve calcular a nova velocidade da particula e somar na posição atual"""

        random1 = np.random.uniform(0.0, 1.0, len(self.get_position()))
        random2 = np.random.uniform(0.0, 1.0, len(self.get_position()))

        inertial_part = inertial * self._velocity   # aplicando a inércia na velocidade da particula
        personal_information = ci * random1 * (self._personal_best_position - self._position)   # calculando a nova velocidade da particula a partir dos auto valores
        global_information = si * random2 * (global_best_particle - self._position)  # calculando a nova velocidade da particula a partir do coletivo

        self.set_velocity(inertial_part + personal_information + global_information, function_optimization)  # atualizando a velocidade da particula
        self.set_position(self._position + self._velocity, function_optimization)    # atualizando a posição da particula




