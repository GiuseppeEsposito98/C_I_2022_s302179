# LAB 2: Set Covering - Genetic algorithm.
### Francesco Scalera(S292432), Giuseppe Esposito(S302179), Filippo Maria Cardano (S292113)

Given a number N and some lists of integers P = (L_0, L_1, L_2, ..., L_n),
determine, if possible, S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n}),
such that each number between 0 and N-1 appears in at least one list.

We designed a genetic algorithm with respect to the professor's code applying the following chagnes:

## Initial population
In the population individual are represented as a tuple which contains the value of the fitness of the individual, a mask of booleans which represents whether a list is part of the individual and a label that describes the tweak type (mutation, crossover or initial).
We randomly selected a viable individuals of the size of the population that we wanted, the viability is based on capability of an individual to provide a possible solution to the problem (with suboptimal fitness values). 

## Fitness metric and feasibility
Our fitness metric is based on the lenght of the selected list inside an individual. Note that we calculate fitness only on individuals that are feasible solutions. Within our population and offspring pool we only have feasible solutions that is individuals that provide a solution to the problem, unfeasible individuals are discarded.
DEF (feasible individual): Given a goal based on N we checked if all allele in the individual covers the target

## Mutation and Crossover
The functions for mutation and crossover are based on the onemax example from the professor's lecture. The parent on which we apply the genetic operator are chosen with a tournament selection. 

## Main parameters
We performed a grid search based on a dictionary with the following parameters:
    N: problem size
    POPULATION_SIZE: size of the initial population and of the population after the pruning
    OFFSPRING_SIZE: number of offsprings generated at each iteration before pruning
    ITERATIONS: number of generations




