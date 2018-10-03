import numpy as np


class Particle:
    def __init__(self, lower_limit, upper_limit, particle_length):
        self._position = np.random.uniform(lower_limit, upper_limit, particle_length)
        self._value = np.inf
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit
        self._particle_length = particle_length
        self._velocity = np.zeros(particle_length)
        self._personal_best_position = self._position.copy()
        self._personal_best_value = np.inf

    def __eq__(self, other):
        return self._personal_best_value == other.get_personal_best_value()

    def __lt__(self, other):
        return self._personal_best_value < other.get_personal_best_value()

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = np.clip(position, self._lower_limit, self._upper_limit)  # espelhando valores menores ou maiores que a função permite para o minimo e máximo.

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.update_personal_best()

    def get_velocity(self):
        return self._velocity

    def get_personal_best_position(self):
        return self._personal_best_position

    def get_personal_best_value(self):
        return self._personal_best_value

    def get_personal_best_information(self):
        return np.array([(self._personal_best_position < 0.5).sum(), (self._personal_best_position >= 0.5).sum()])

    def update_personal_best(self):
        """ se a posição atual for melhor que a melhor posição da particula, então deve receber a nova posição """
        if self._value <= self._personal_best_value:
            self._personal_best_value = self._value
            self._personal_best_position = self._position

    def update_particle(self, global_best_particle, inertial, ci, si):
        """ Deve calcular a nova velocidade da particula e somar na posição atual"""

        random1 = np.random.uniform(self._lower_limit, self._upper_limit, self._particle_length)
        random2 = np.random.uniform(self._lower_limit, self._upper_limit, self._particle_length)

        inertial_part = inertial * self._velocity   #aplicando a inércia na velocidade da particula
        personal_information = ci * random1 * (self._personal_best_position - self._position)   #calculando a nova velocidade da particula a partir dos auto valores
        global_information = si * random2 * (global_best_particle - self._position) #calculando a nova velocidade da particula a partir do coletivo

        self._velocity = inertial_part + personal_information + global_information #atualizando a velocidade da particula
        self.set_position(self._position + self._velocity)    #atualizando a posição da particula




