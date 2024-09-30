import random
import math

input_file = open("input.txt")
output_file = open("Output_1.txt", "w")

input_data = input_file.readlines()
time_class_lengths = input_data[0].strip().split(' ')
time_length = int(time_class_lengths[0])
class_length = int(time_class_lengths[1])

population = {}
if class_length <= time_length:
    for i in range(0, 150):
        chromosome = ''
        for j in range(0, time_length * class_length):
            chromosome += str(random.randint(0, 1))
        population[chromosome] = 0

def overlap_penalty(sequence):
    penalty_score = 0
    for i in range(0, int(len(sequence) / time_length)):
        overlap_flag = 0
        for j in range(i, len(sequence), 3):
            if sequence[j] == '1':
                overlap_flag += 1
        if overlap_flag > 0:
            penalty_score += (overlap_flag - 1)
    return penalty_score

def consistency_penalty(sequence):
    penalty_score = 0
    for i in range(0, len(sequence), 3):
        consistency_flag = 0
        for j in range(i, i + 3):
            if sequence[j] == '1':
                consistency_flag += 1
        if consistency_flag > 0:
            penalty_score += (consistency_flag - 1)
    return penalty_score

fitness_values = []
def calculate_fitness(sequence):
    fitness_penalty = -(overlap_penalty(sequence) + consistency_penalty(sequence))
    fitness_values.append((sequence, fitness_penalty))
    return fitness_penalty

def perform_crossover(parent_1, parent_2):
    midpoint = int(len(parent_1) / 2)
    offspring_1 = parent_1[:midpoint] + parent_2[midpoint:]
    offspring_2 = parent_1[midpoint:] + parent_2[:midpoint]
    population[offspring_1] = 0
    population[offspring_2] = 0
    return offspring_1, offspring_2

def apply_mutation(sequence):
    sequence_list = list(sequence)
    
    mutation_point = random.randint(0, len(sequence_list) - 1)
    
    sequence_list[mutation_point] = str(1 - int(sequence_list[mutation_point]))
    
    mutated_sequence = ''.join(sequence_list)
    
    return mutated_sequence


def genetic_algorithm_iteration(parent_1, parent_2, limit):
    child_x, child_y = perform_crossover(parent_1, parent_2)
    if calculate_fitness(child_x) == 0:
        return child_x
    elif calculate_fitness(child_y) == 0:
        return child_y
    else:
        limit -= 1
        if limit == 0:
            return "000000000"
        child_x = apply_mutation(child_x)
        child_y = apply_mutation(child_y)
        return genetic_algorithm_iteration(child_x, child_y, limit)

random_x = list(population.keys())[random.randint(0, len(population) - 1)]
random_y = list(population.keys())[random.randint(0, len(population) - 1)]
final_result = genetic_algorithm_iteration(random_x, random_y, 1000)

if final_result in ["000000000", "111111111"]:
    print('-100', file=output_file)
else:
    print(final_result, file=output_file)
    for seq, fit in fitness_values:
        if seq == final_result:
            print(fit, file=output_file)

input_file.close()
output_file.close()
