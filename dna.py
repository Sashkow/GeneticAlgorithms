from collections import UserList, UserDict

import random

class Dna(object):
	pass
	
	
class ListDna(Dna, UserList):
	default_initial_size = 10
	"""DNA sequence in a genetic algorithm"""
	def __init__(self, data = None):
		super().__init__()
		if data == None:
			data = ListDna.default_initial_size
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
	return ListDna(a[:poc] + b[poc:]), ListDna(b[:poc] + a[poc:])


class DictDna(Dna, UserDict):
	max_inital_size = 10 
	def __init__(self, data=None):
		super().__init__()
		if data == None:
			data = random.randrange(DictDna.max_inital_size + 1)
		
		if isinstance(data, int):
			initial_size = data
			self.data = {float(i)/initial_size : random.randrange(0,2) 
						for i in range(initial_size)}
		elif isinstance(data, dict):
			self.data = data

		self.fitness_function = self.dummy_fitness_function
	
	def dummy_fitness_function(self):
		return sum(self.values())


def different_length_crossover(a, b, start=None, end=None):
	if start == None or end == None:
		rnd1 = random.random()
		rnd2 = random.random()
		start, end = min(rnd1,rnd2), max(rnd1,rnd2)
	# print(a, b, start,end)
	cut_from_a = {k: v for k, v in a.items() if start<k<end }
	new_a = {k: v for k, v in a.items() if not (start<k<end) }

	cut_from_b = {k: v for k, v in b.items() if start<k<end }
	new_b = {k: v for k, v in b.items() if not (start<k<end) }

	new_a.update(cut_from_b)
	new_b.update(cut_from_a)
	assert(len(a) + len(b) == len(new_a) + len(new_b))
	return new_a, new_b
