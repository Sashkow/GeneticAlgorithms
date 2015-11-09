from collections import UserList, UserDict
from gene import BoolGene, NK_Gene


import random

class Dna(object):
	"""
	must have:
		fitness_function method 
		mute method
		crossover method
	"""
	pass


def dummy_fitness_function_for_list_dna(list_dna):
	"""
	default fitness function
	assumes GeneClass to be BoolGene
	"""
	return sum([g.data for g in list_dna])

def dummy_fitness_function_for_dict_dna(dict_dna):
	"""
	default fitness function
	assumes GeneClass to be BoolGene
	"""
	return sum([dict_dna[index].data for index in dict_dna])

def dummy_fitness_function_for_nk_dna(nk_dna):
	"""
	default fitness function for class NK_Dna 
	returns automata stability to outer perturbations
	"""
	return nk_dna.automata.stability


class ListDna(Dna, UserList):
	default_dna_size = 5
	"""constant sized DNA sequence in a genetic algorithm"""
	def __init__(self, GeneClass=BoolGene, **kwargs):
		"""
		optional arguments:
			dna_size -- amount of genes in dna
			data -- plain list of Gene objects or 
			  		of plain data if GeneClass is can change types
	  		if both of these optional arguments are set then size is ignored

	  		fitness_function -- fitness function
		"""
		super().__init__()
		if len(kwargs) == 0:
			self._dna_size = ListDna.default_dna_size
			self.data = [GeneClass.generate_random() 
					 for i in range(self._dna_size)] 	


		if "dna_size" in kwargs:
			self._dna_size = kwargs["dna_size"]
			self.data = [GeneClass.generate_random() 
					 for i in range(self._dna_size)] 	

		if "data" in kwargs:
			self.data = list([GeneClass(item) for item in kwargs["data"]])

		self.fitness_function = dummy_fitness_function_for_list_dna

	
	def mute(self, mutation_probability):
		for gene in self:
			if random.random() < mutation_probability:
				gene.mute()

	def crossover(a, b, cross_lst=[]):
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
		return ListDna(data=a[:poc] + b[poc:]), \
			   ListDna(data=b[:poc] + a[poc:])



class DictDna(Dna, UserDict):
	"""variable sized DNA sequence in a genetic algorithm"""
	max_inital_size = 10 
	
	def __init__(self, GeneClass=BoolGene, **kwargs):
		"""
		arguments:
			GeneClass -- class for genes in dna. Default is BoolGene
		optional arguments:
			size -- amount of genes in dna
			data -- plain list of Gene objects or 
			  		of plain data if GeneClass is can change types
	  		if both optional arguments are set then size is ignored
		"""
		super().__init__()
		_dna_size = 0
		self.data = {}

		# if len(kwargs) == 0:
		# 	_dna_size = random.randrange(1, DictDna.max_inital_size + 1)
		# 	self.data = dict({(float(i)/(_dna_size)):
		# 					   GeneClass.generate_random() 
		# 			 		   for i in range(_dna_size)})	
		

		if "dna_size" in kwargs:
			_dna_size = kwargs["dna_size"]
			self.data = dict({(float(i)/(_dna_size)):
							   GeneClass.generate_random() 
					 		   for i in range(_dna_size)})	

		if "data" in kwargs:
			data = kwargs["data"]
			if isinstance(data, list):
				_dna_size = len(data)
				self.data = dict({(float(i)/(_dna_size)):
								   data[i]
						 		   for i in range(_dna_size)})	
			if isinstance(data, dict):
				self.data = data

		self.fitness_function = dummy_fitness_function_for_dict_dna

	def mute(self, mutation_probability):
		for index in self:
			if random.random() < mutation_probability:
				self[index].mute()
	
	def crossover(a, b, start=None, end=None):
		if start == None or end == None:
			rnd1 = random.random()
			rnd2 = random.random()
			start, end = min(rnd1,rnd2), max(rnd1,rnd2)
		# print(a, b, start, end)
		cut_from_a = {k: v for k, v in a.items() if start<k<end }
		new_a = {k: v for k, v in a.items() if not (start<k<end) }

		cut_from_b = {k: v for k, v in b.items() if start<k<end }
		new_b = {k: v for k, v in b.items() if not (start<k<end) }

		new_a.update(cut_from_b)
		new_b.update(cut_from_a)
		assert(len(a) + len(b) == len(new_a) + len(new_b))

		return DictDna(data=new_a), DictDna(data=new_b)


class NK_Dna(DictDna):
	"""
	dna based on S.Kauffman's NK-automata(network)
	"""
	def __init__(self, automata):
		data = []
		for i in range(len(automata.functions_list)):	
			bool_function = automata.functions_list[i]
			links = automata.links_list[i]
			data.append(NK_Gene(bool_function=bool_function,
								links=links))

		super().__init__(data=data)
		assert(type(self.data), dict)
		
		self.GeneClass = NK_Gene
		self.automata = automata

		self.fitness_function = dummy_fitness_function_for_nk_dna

	




		







