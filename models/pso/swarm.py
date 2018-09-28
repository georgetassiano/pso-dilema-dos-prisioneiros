import math

class Swarm:

    def __init__(self, numberOfParticles=2):
        self.globalBestParticle = []
        self.globalBestValue = math.inf
        self.particles = []

    def initParticles(self):
