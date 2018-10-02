import math
import numpy as np


class Particle:
    def __init__(self, particleLength=2):
        self._position = np.random.uniform(0.0, 1.0, particleLength)
        self._value = math.inf
        self._velocity = np.array([])
        self._personal_best_position = np.array([])
        self._personal_best_value = math.inf

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.update_personal_best()

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_personal_best_position(self):
        return self._personal_best_position

    def get_personal_best_value(self):
        return self._personal_best_value

    def update_personal_best(self):
        if self._value <= self._personal_best_value:
            self._personal_best_value = self._value
            self._personal_best_position = self._position

    def update_particle(self, global_best_particle, inertial, ci, si):
        random1 = 1.0
        random2 = 1.0
        inertial_part = inertial * self._velocity
        personal_information = ci*random1*(self._personal_best_position - self._position)
        global_information = si*random2*(global_best_particle - self._position)
        self._velocity = inertial_part + personal_information + global_information
        self._position += self._velocity


