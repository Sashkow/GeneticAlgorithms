from collections import UserList
from dna import ListDna

class Population(UserList):
	"""Population of DNA sequences in a genetic algorithm"""
	def __init__(self, DnaClass=ListDna, initial_size=10):
		super().__init__()
		self.DnaClass = DnaClass
		self.initial_size = initial_size
		self.data = []
		self.init_population()

	def init_population(self):
		self.data = [self.DnaClass() for i in range(self.initial_size)]

	def step(self):
		"""
		sort dna by fitness
		"""


