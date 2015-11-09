from collections import UserList
from dna import ListDna
from gene import BoolGene
import random


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
		whatever arguments needed for DnaClass

	"""
	def __init__(self, DnaClass=ListDna,
					   GeneClass=BoolGene,
					   population_size=10,
					   part_selected=.5,
					   mutation_probability=0,
					   generations=1000,
					    **kwargs):
		super().__init__()

		self.DnaClass = DnaClass
		self.population_size = population_size
		self.data = [DnaClass(GeneClass=BoolGene, **kwargs)
					 for i in range(self.population_size)]

		self.part_selected = part_selected
		self.mutation_probability = mutation_probability
		self.generations = generations

		

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
		amt_selected = \
		  int(self.population_size * self.part_selected) 

		spawning_pool = [] 		# list of dna selected for reproduction
		new_data = []
		sorted_dna = sorted(self.data, 
			   			   key=lambda dna: dna.fitness_function(dna),
			   			   reverse=True)
		spawning_pool = sorted_dna[:amt_selected]
		
		

		# mutation
		for dna in spawning_pool:
			dna.mute(self.mutation_probability)

		# crossover
		while len(new_data) < \
			  self.population_size - (self.population_size % 2):
			d1, d2 = self.DnaClass.crossover(
						spawning_pool[random.randrange(len(spawning_pool))],
						spawning_pool[random.randrange(len(spawning_pool))])
			new_data += [d1, d2]
		if (self.population_size % 2) == 1:
			new_data.append(
			  spawning_pool[random.randrange(len(spawning_pool))])

		assert(len(self.data) == len(new_data))
		self.data = new_data


	def iterate(self):
		"""
		repeats step method generations times
		"""
		for i in range(self.generations):
			print([item.fitness_function() for item in self])
			self.step()
			









