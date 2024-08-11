import random

# Number of individuals in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated
TARGET = "I love GeeksforGeeks"

class Individual:
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
    
    @classmethod
    def mutated_genes(cls):
        '''
        Create random genes for mutation
        '''
        return random.choice(GENES)
    
    @classmethod
    def create_gnome(cls):
        '''
        Create chromosome or string of genes
        '''
        gnome_len = len(TARGET)
        return [cls.mutated_genes() for _ in range(gnome_len)]
    
    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome)
    
    def cal_fitness(self):
        '''
        Calculate fitness score
        '''
        return sum(gs != gt for gs, gt in zip(self.chromosome, TARGET))

def main():
    global POPULATION_SIZE
    
    generation = 1
    found = False
    population = []
    
    # Create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))
    
    while not found:
        # Sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)
        
        if population[0].fitness <= 0:
            found = True
            break
        
        # Generate new offsprings for the new generation
        new_generation = []
        
        # Perform Elitism
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])
        
        # Produce offspring from 50% of the fittest population
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        
        population = new_generation
        
        print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")
        generation += 1

if __name__ == "__main__":
    main()
