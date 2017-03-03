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

class LetterGene(object):
	letters = ['A', 'T', 'G', 'C']

	def __init__(self, data=''):
		if isinstance(data, IntGene):
			assert(len(data.data) == 1)
			self.data = data.data
		else:
			if not data:
				self.data = random.choice(LetterGene.letters)
			else:
				assert(len(data) == 1)
				self.data = data

	def __str__(self):
		return self.data

	def __repr__(self):
		return self.data

	def mute(self):
		self.data = random.choice(LetterGene.letters)

	def generate_random():
		return LetterGene(random.choice(LetterGene.letters))




class IntGene(Gene):

	def __init__(self, data=0, minval=0, maxval=0):
		if isinstance(data, IntGene):
			self.data = data.data
		else:
			self.data = int(data)

		self.min = minval
		self.max = maxval

	def __str__(self):
		return self.data

	def mute(self):
		self.data = int(random.randrange(minval, maxval + 1))

	def generate_random(minval, maxval):
		return BoolGene(int(random.randrange(minval, maxval)))


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




