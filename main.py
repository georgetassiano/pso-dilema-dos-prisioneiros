from models.pso.pso_algorithm import PSOAlgorithm
from models.pso.swarm import Swarm
from models.functions_optimization.function_optimization_dp_individual_base import FunctionOptimizationDPIndividualBase as DPIndividual
from models.functions_optimization.function_optimization_dp_coletivo_base import FunctionOptimizationDPColetivoBase as DPColetivo
import matplotlib.pyplot as plt
import numpy as np

particles_length = 50  # quantidade de particulas
global_comparison_length_10 = round(particles_length * 0.1)  # quantidade de particulas para comparar (10%)
global_comparison_length_30 = round(particles_length * 0.3)  # quantidade de particulas para comprar (30%)
lower_limit = 0.0  # limite inferior da função
upper_limit = 1.0  # limite superior da função
max_interation = 1000  # máximo de interações
max_execution = 5  # máximo de execuções

c = 3  # quantidade de posições cooperativas para aplicação de 1 bonus
bonus = -0.5  # bonus a ser dado por cada bonus a ser dado
inertial_ini = 1.2  # valor da variável de inércia inicial
inertial_final = 0.8  # valor da variável de inércia final
ci = 1.0  # valor da constante da relevância da informação pessoal
si = 1.0  # valor da constante de relevância da informações social

if __name__ == '__main__':
    ci = 1.0  # valor da constante da relevância da informação pessoal
    si = 1.0  # valor da constante de relevância da informações social

    functions_optimization = []
    functions_optimization.append([DPColetivo(lower_limit, upper_limit), 'Coletivo'])
    functions_optimization.append(
        [DPColetivo(lower_limit, upper_limit, global_comparison_length=global_comparison_length_10), 'Coletivo 10'])
    functions_optimization.append(
        [DPColetivo(lower_limit, upper_limit, global_comparison_length=global_comparison_length_30), 'Coletivo 30'])
    functions_optimization.append([DPIndividual(lower_limit, upper_limit), 'Individual'])
    functions_optimization.append(
        [DPIndividual(lower_limit, upper_limit, global_comparison_length=global_comparison_length_10), 'Individual 10'])
    functions_optimization.append(
        [DPIndividual(lower_limit, upper_limit, global_comparison_length=global_comparison_length_30), 'Individual 30'])

    for e in range(len(functions_optimization)):
        algorithm = PSOAlgorithm(functions_optimization[e][0], max_interation, max_execution)
        algorithm.exec_algorithm(particles_length, functions_optimization[e][0], inertial_ini, inertial_final, ci, si)

        best, err_best = algorithm.get_best()
        avarage, err_avarage = algorithm.get_avarage()
        lowest, err_lowest = algorithm.get_lowest()
        entropy = algorithm.get_entropy()

        plotarBar = [avarage[0], avarage[max_interation // 2], avarage[-1]]

        plt.figure(e)

        plt.subplot(311)
        plt.title(f'Pensamento {functions_optimization[e][1]} com entropia={entropy}')
        plt.plot(best, 'r-', label='melhor')
        plt.plot(avarage, 'b-', label='média')
        plt.plot(lowest, 'g-', label='pior')
        plt.xlabel('nº iteração')
        plt.ylabel('nº cooperações')
        plt.legend()

        plt.subplot(312)
        plt.errorbar(np.arange(max_interation), avarage, yerr=err_avarage)
        plt.xlabel('nº iteração')
        plt.ylabel('nº cooperações')

        plt.subplot(313)
        plt.bar(np.arange(3), plotarBar)
        plt.xticks(np.arange(3), ('inicial', 'meio', 'fim'))
        plt.show()



