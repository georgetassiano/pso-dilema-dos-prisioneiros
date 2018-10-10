from models.pso.particle import Particle
import numpy as np

class Swarm:

    def __init__(self, number_of_particles, function_optimization, inertial, ci, si):
        self._number_of_particles = number_of_particles
        self._particles = self.initParticles(number_of_particles, function_optimization)
        self._global_best_particle = self._particles[0].get_personal_best_position()
        self._global_best_value = self._particles[0].get_personal_best_value()
        self._function_optimization = function_optimization
        self._inertial = inertial
        self._ci = ci
        self._si = si

    def get_particles(self):
        return self._particles

    def get_global_best_particle(self):
        return self._global_best_particle

    def get_global_best_value(self):
        return self._global_best_value

    def get_information(self):
        best = self.get_particles()[0].get_position_information()
        avarage = np.zeros(2)
        for i in self.get_particles():
            avarage += i.get_position_information()
        avarage = avarage / self._number_of_particles
        lowest = self.get_particles()[-1].get_position_information()
        return np.array([best, avarage, lowest])

    def initParticles(self, number_of_particles, function_optimization):
        particles = []
        array = []
        for i in range(number_of_particles):
            particle = Particle(function_optimization.get_min_limit(), function_optimization.get_max_limit(), function_optimization.get_count_params())
            particles.append(particle)
            array.append(particle.get_position())
        for i in particles:
            i.set_value(function_optimization.calc_result(particle.get_position(), array))
        particles = sorted(particles)
        return particles

    def updateSwarm(self):
        array = []
        for i in self._particles:
            array.append(i.get_position())
        for i in self._particles:
            i.update_particle(self._global_best_particle, self._inertial, self._ci, self._si)
            i.set_value(self._function_optimization.calc_result(i.get_position(), array))
        self._particles = sorted(self._particles)
        if self._particles[0].get_personal_best_value() <= self._global_best_value:
            self._global_best_particle = self._particles[0].get_personal_best_position()
            self._global_best_value = self._particles[0].get_personal_best_value()

