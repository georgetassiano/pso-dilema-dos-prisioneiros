import math
from models.pso.swarm import Swarm
class PSOAlgorithm:
    def __init__(self, inertia=1.2, ci=2, si=2, maxInteration=1000):
        self.inertia = inertia
        self.ci = ci
        self.si = si
        self.maxInteration = maxInteration
        self.swarm = None

    def initSwarm(self):
        self.swarm = Swarm(10)
        self.swarm.initParticles()
