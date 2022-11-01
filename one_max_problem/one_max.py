import random
from tkinter import OFF 

PROBLEM_SIZE = 10
POPULATION_SIZE = 30
OFFSPRING_SIZE = 20 

def onemax(genome):
    return sum(genome)

print(onemax([1,2,3,4,5]))
# this is a separable problem

# define a populatio (set of individuals) 
# in our case the individual is a tuple
# we use a steady state approach 
# we do not generate a lot, we just generate some individuals and we need to keep some of them 

def select_parent(population, tournament_size = 2):
    subset = random.choice(population, k = tournament_size)
    return max(subset, key=lambda i: i [1])

def cross_over(g1,g2):
    g1, g2 = p1[0], p2[0]
    cut = random.randint(0,PROBLEM_SIZE)
    return g1[:cut] + g2[cut:]

def mutation(g):
    point = random.randint(0,PROBLEM_SIZE-1)
    return g[:point] + (1-g[point],) + g[point+1:]



genome = [tuple(random.choice([1,0]) for _ in range(PROBLEM_SIZE)) for __ in range(POPULATION_SIZE)]
print(genome)
population = list()
for individual in genome:
    population.append((genome, onemax(genome)))

for i in range(OFFSPRING_SIZE):
    if random.random() < .3:
       p = select_parent(population) 
       offspring = mutation(p[0])
    else:
        p1 = select_parent(population)
        p2 = select_parent(population)
        offspring = cross_over(p1[0],p2[0])
    population.append((offspring,onemax(offspring)))

population = sorted(population, key= lambda i: i[1], reversed= True)

# when all individuals have all the same genome we need to come up with a kind of mutation

