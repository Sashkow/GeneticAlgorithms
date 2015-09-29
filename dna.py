from collections import UserList
import random


class Dna(UserList):
	"""DNA sequence in a genetic algorithm"""
	default_initial_size = 10
	def __init__(self, data=default_initial_size):
		super(UserList, self).__init__()
		if isinstance(data, int):
			initial_size = data 
			self.data = [random.randrange(0,1) for i in range(initial_size)] 
		elif isinstance(data, list):
			self.data = data

		self.fitness_function = self.dummy_fitness_function
	
	def dummy_fitness_function(self):
		return sum(self)


def crossover(a, b, cross_lst=[], ):
	"""
	a -- Dna object
	b -- Dna object
	cross_lst  -- list of points of crossover

	a and b should be of the same length

	return genetic recombination of two DNA's
	"""
	if cross_lst == []:
		cross_lst = [random.randrange(len(a))]

	poc = cross_lst[0]
	return Dna(a[:poc] + b[poc:]), Dna(b[:poc] + a[poc:])









		
		
