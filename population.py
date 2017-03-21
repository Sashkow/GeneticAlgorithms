from collections import UserList
from dna import ListDna
from gene import BoolGene
import random
import copy


class Population(UserList):
    """
    Population of DNA sequences in a genetic algorithm
    arguments:
        DnaClass -- class for DNA, e.g. ListDna or DictDna
        GeneClass -- class for gene, e.g BoolGene
        population_size -- initial size of the population
        part_selected -- amount of dna selected for reproduction
        mutation_probability -- mutation probability per gene
        generations -- generations amount to iterate algorithm through
        

    other arguments:
        whatever arguments needed for DnaClass e.g fitness_function

    """
    def __init__(self, DnaClass=ListDna,
                       GeneClass=BoolGene,
                       population_size=10,
                       part_selected=0.5,
                       mutation_probability=0,
                       generations=10,
                        **kwargs):

        

        super().__init__()

        self.DnaClass = DnaClass
        self.population_size = population_size
        
        self.data = [DnaClass(GeneClass=GeneClass, **kwargs)
                     for i in range(self.population_size)]


        

        self.part_selected = part_selected
        self.mutation_probability = mutation_probability
        self.generations = generations



    def pick(self):
        lst = [dna.fitness_function(dna) for dna in self]
        fitness_sum = sum(lst)
        pick_at = random.uniform(0, fitness_sum)
        current = 0
        for dna in self:
            current += dna.fitness_function(dna)
            if current > pick_at:
                return dna


    def step(self):
        """
        a method that performs one iteration of the algorithm

        sorts population
        selects some part of the fittest dna
        performs random mutations on dna with some probability
        picks pairs of random dna from selection, crossover them
            until needed population length is reached

        this method conserves population size
        """
        # amt_selected = \
        #   int(self.population_size * self.part_selected) 

        # spawning_pool = []      # list of dna selected for reproduction
        new_data =[]
        
        sorted_dna = sorted(self.data, 
                           key=lambda dna: dna.fitness_function(dna),
                           reverse=True)
        
        
        

        # mutation
        for dna in sorted_dna:
            dna.mute(self.mutation_probability)

        # crossover
        while len(new_data) < \
                self.population_size - (self.population_size % 2):

            d1 = copy.copy(self.pick())
            d2 = copy.copy(self.pick())
            times = 2
            for i in range(times):
                d1.crossover(d2)

            new_data += [d1, d2]





        if (self.population_size % 2) == 1:
            new_data.append(copy.deepcopy(self.pick()))

        assert(len(self.data) == len(new_data))

        for i in range(len(new_data)):
            self.data[i].data = new_data[i]


    def iterate(self):
        """
        repeats step method generations times
        """
        for i in range(self.generations):
            sorted_polulation = sorted(self.data, key=lambda item: - item.fitness_function(item))
            print(
                    [item.to_string() for item in sorted_polulation[:8]],
                    [round(item.fitness_function(item),2) for item in sorted_polulation]
            )

            # print([item.to_string() for item in self.data])

            self.step()
        print("result")
        sorted_polulation = sorted(self.data, key=lambda item: - item.fitness_function(item))
        print([str(item) for item in sorted_polulation])


