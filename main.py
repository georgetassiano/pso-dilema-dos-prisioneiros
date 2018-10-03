from models.pso.pso_algorithm import PSOAlgorithm
from models.pso.swarm import Swarm
from models.functions_optimization.dp_individual_sem_bonus import DPIndividualSemBonus
import matplotlib.pyplot as plt
import numpy as np

particles_length = 50
count_parms = 30
valueIndividual = 1.2 * count_parms
valueColetivo = 0 * count_parms
valueBonus = (count_parms // 3) * -0.5
array = np.zeros(count_parms)
list = np.zeros([50, count_parms])
c = 3
bonus = -0.5
global_comparison_length = 1
lower_limit = 0.0
upper_limit = 1.0
inertial = 1.0
ci = 1.0
si = 1.0

if __name__ == '__main__':
    function1 = DPIndividualSemBonus(lower_limit, upper_limit, count_parms, global_comparison_length)
    swarm = Swarm(particles_length, function1, inertial, ci, si)
    algorithm = PSOAlgorithm(swarm, function1, 1000)
    algorithm.exec_algorithm()
    result = algorithm.get_result()
    plotarBest = np.zeros([np.size(result, 0)])
    plotarAvarege = np.zeros([np.size(result, 0)])
    plotarLowest = np.zeros([np.size(result, 0)])
    for i in range(np.size(result, 0)):
        plotarBest[i] = result[i][0][0]
        plotarAvarege[i] = result[i][1][0]
        plotarLowest[i] = result[i][2][0]

    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotarBest, 'r--', plotarAvarege, 'bs', plotarLowest, 'g^')
    plt.subplot(212)
    plotarBar = [result[0][2][0], result[500][2][0], result[-1][2][0]]
    plt.bar(np.arange(3), plotarBar)
    plt.xticks(np.arange(3), ('initial', 'medium', 'final'))
    plt.show()



