import random

from cell_modelling.boolfunction import BoolFunction

class Gene(object):
	"""
	gene class must have:
		data field
		mute method for random mutation
		static generate_random that generates random instance of a class
	"""
	pass

class BoolGene(Gene):
	def __init__(self, data=False):
		if isinstance(data, BoolGene):
			self.data = data.data
		else:
			self.data = bool(data)

	def __str__(self):
		return self.data

	def __repr__(self):
		return str(self.data)

	def mute(self):
		self.data = not self.data

	def generate_random():
		return BoolGene(bool(random.randrange(0, 2)))


class NK_Gene(Gene):
	def __init__(self, bool_function, links):
		assert(type(bool_function) == BoolFunction)
		assert(type(links) == list)
		self.bool_function = bool_function
		self.links = links




