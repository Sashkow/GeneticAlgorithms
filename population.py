from collections import UserList
from dna import Dna

class Population(UserList):
	"""Population of DNA sequences in a genetic algorithm"""
	def __init__(self, initial_size=10):
		super(UserList, self).__init__()
		self.initial_size = initial_size
		self.data = []
		self.init_population()

	def init_population(self):
		self.data = [Dna() for i in range(self.initial_size)]









	
