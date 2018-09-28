import math
import random
class Particle:
    def __init__(self, particleLength=2):
        self.particleLength = particleLength
        self.position = []
        self.value = math.inf
        self.velocity = []
        self.personalBestPosition = []
        self.personalBestValue = math.inf

    def initParticle(self):
        for i in range(self.particleLength):
            self.positions[i] = random.uniform(0.0,1.0)

    def updateVelocity(self, globalBestParticle, inertial, ci, si):
        self.velocity = inertial * self.velocity + ci*random.uniform(0.0,1.0)*(self.personalBestPosition - self.position) + si*random.uniform(0.0,1.0)*(globalBestParticle - self.position)