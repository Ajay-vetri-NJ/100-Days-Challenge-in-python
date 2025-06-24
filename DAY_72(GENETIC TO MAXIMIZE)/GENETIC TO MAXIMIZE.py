import numpy as np

def fitness_function(x):
    return x ** 2

def generate_population(size, lower_bound, upper_bound):
    return np.random.uniform(lower_bound, upper_bound, size)

def select_individuals(population, fitness_scores, num_individuals):
    selected_indices = np.argsort(fitness_scores)[-num_individuals:]
    return population[selected_indices]

def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if np.random.rand() < mutation_rate:
        mutation_value = np.random.uniform(lower_bound, upper_bound)
        individual += mutation_value
    return individual

population_size = 10
num_generations = 50
mutation_rate = 0.1
num_parents = 2
lower_bound = -10
upper_bound = 10

population = generate_population(population_size, lower_bound, upper_bound)

for generation in range(num_generations):
    fitness_scores = np.array([fitness_function(ind) for ind in population])
    
    parents = select_individuals(population, fitness_scores, num_parents)
    
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = np.random.choice(parents, 2, replace=False)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring, mutation_rate, lower_bound, upper_bound)
        new_population.append(offspring)
    
    population = np.array(new_population)

    best_fitness = np.max(fitness_scores)
    best_individual = population[np.argmax(fitness_scores)]
    print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Individual = {best_individual}")

print(f"\nOptimal Solution: x = {best_individual}, f(x) = {fitness_function(best_individual)}")
