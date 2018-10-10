from models.pso.pso_algorithm import PSOAlgorithm
from models.pso.swarm import Swarm
from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase as DPIndividual
from models.functions_optimization.function_optimization_dp_coletivo_base import FunctionOptimizationDPColetivoBase as DPColetivo
import matplotlib.pyplot as plt
import numpy as np

count_parms = 30  # tamanho da representacao das particulas
particles_length = 50  # quantidade de particulas
global_comparison_length = 1  # quantidade de particulas para comparar
global_comparison_length_10 = round(particles_length * 0.1)  # quantidade de particulas para comparar (10%)
global_comparison_length_30 = round(particles_length * 0.3)  # quantidade de particulas para comprar (30%)
lower_limit = 0.0  # limite inferior da função
upper_limit = 1.0  # limite superior da função
max_interation = 1000  # máximo de interações
max_execution = 5  # máximo de execuções

c = 3.0  # quantidade de posições cooperativas para aplicação de 1 bonus
bonus = -0.5  # bonus a ser dado por cada bonus a ser dado
inertial = np.float_(1.2)  # valor da variável de inércia
ci = np.float_(1.0)  # valor da constante da relevância da informação pessoal
si = np.float_(1.0)  # valor da constante de relevância da informações social

if __name__ == '__main__':
    function1 = DPIndividual(lower_limit, upper_limit, count_parms)
    swarm = Swarm(particles_length, function1, inertial, ci, si)
    algorithm = PSOAlgorithm(swarm, function1, max_interation, max_execution)
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



