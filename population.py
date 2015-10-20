from collections import UserList
from dna import ListDna
import random

class Population(UserList):
	"""Population of DNA sequences in a genetic algorithm"""
	def __init__(self, DnaClass=ListDna, initial_size=5):
		super().__init__()
		self.DnaClass = DnaClass
		self.initial_size = initial_size
		self.data = []
		self.init_population()

	def init_population(self):
		self.data = [self.DnaClass() for i in range(self.initial_size)]

	def step(self):
		"""
		shuffle
		pairwise crossover
		sort dna by fitness, check
		repeat
		"""
		new_data = []

		random.shuffle(self.data)

		#pairwise crossover
		for i in range(1,len(self.data)-1,2):
			d1, d2 = self.DnaClass.crossover(self.data[i-1], self.data[i])
			new_data += [d1,d2]
		if (len(self.data) % 2) == 1:
			new_data.append(self.data[-1])

		#sort
		new_data = sorted(new_data, key=lambda dna: dna.fitness_function(), reverse=True)

		#cut half and duplicate; this step is a bit arbitrary TODO
		is_odd_data = (len(new_data)/2 != 0)
		new_data = new_data[:int(len(new_data)/2)] + new_data[:int(len(new_data)/2)]

		if is_odd_data:
			new_data.append(new_data[-1])

		self.data = new_data


	def iterate(self):
		for i in range(10):
			print([item.fitness_function() for item in self])
			self.step()
			









