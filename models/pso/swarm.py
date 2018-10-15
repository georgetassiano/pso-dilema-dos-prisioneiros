from models.pso.particle import Particle
import numpy as np

class Swarm:

    def __init__(self, number_of_particles, function_optimization, inertial_ini, inertial_final, ci, si):
        self._number_of_particles = number_of_particles  # numero de particulas
        self._particles = self.initParticles(number_of_particles, function_optimization)  # população das particulas
        self._global_best_particle = self._particles[0].get_personal_best_position()  # melhor posição global de particula
        self._global_best_value = self._particles[0].get_personal_best_value()  # melhor valor global
        self._function_optimization = function_optimization  # função de otimização
        self._inertial_ini = inertial_ini  # valor da inercia inicial
        self._inertial_final = inertial_final  # valor da inercia final
        self._ci = ci  # valor da constante de informação cognitiva
        self._si = si  # valor da constante de informação social

    def get_particles(self):
        return self._particles

    def get_global_best_particle(self):
        return self._global_best_particle

    def get_global_best_value(self):
        return self._global_best_value

    def get_inertial(self, iteration_t, iteration_final):
        """ retorna o valor da inércia a ser usado, conforme a iteração atual e iteração máxima do algoritmo"""
        return self._inertial_ini - (self._inertial_ini - self._inertial_final) * (iteration_t / iteration_final)

    def get_information(self):
        best = self.get_particles()[0].get_position_information()
        avarage = np.zeros(2)
        for i in self.get_particles():
            avarage += i.get_position_information()
        avarage = avarage / self._number_of_particles
        lowest = self.get_particles()[-1].get_position_information()
        return np.array([best, avarage, lowest])

    def initParticles(self, number_of_particles, function_optimization):
        """ inicia as particulas da população """
        particles = []
        array = []
        for i in range(number_of_particles):  # inicia a população de particulas com o array da função
            particle = Particle(function_optimization.generate_array())
            particles.append(particle)
            array.append(particle.get_position())
        for i in particles:  # calcula o desempenho das particulas
            i.set_value(function_optimization.calc_result(i.get_position(), array))
        particles = sorted(particles)  # ordena a população em ordem decrescente de desempenho
        return particles

    def updateSwarm(self, iteration_t, iteration_final):
        """ atualiza as particulas da população """
        array = []
        for i in self._particles:  # recupera o array da população
            array.append(i.get_position())
        for i in self._particles:  # atualiza as particulas
            i.update_particle(self._global_best_particle, self.get_inertial(iteration_t, iteration_final), self._ci, self._si, self._function_optimization)
            i.set_value(self._function_optimization.calc_result(i.get_position(), array))
        self._particles = sorted(self._particles)
        if self._particles[0].get_personal_best_value() <= self._global_best_value: # verifica se um melhor global foi encontrado e atualiza
            self._global_best_particle = self._particles[0].get_personal_best_position()
            self._global_best_value = self._particles[0].get_personal_best_value()

