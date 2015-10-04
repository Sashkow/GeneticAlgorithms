import unittest 

from population import Population
from dna import Dna, ListDna, crossover, DictDna, different_length_crossover

from unittest import TestCase
from pprint import pprint


class TestPopulation(TestCase):
	def test_population_default_constructor(self):
		p = Population()
		self.assertNotEqual(Population(), None)
		self.assertEqual(type(p.data), list)
		self.assertEqual(len(p), p.initial_size)
		if len(p) != 0:
			self.assertEqual(type(p[0]), ListDna)

	def test_populaion_strict_dna_class_constructor(self):
		pl = Population(ListDna)
		if len(pl) != 0:
			self.assertEqual(type(pl[0]), ListDna)
		pd = Population(DictDna)
		if len(pd) != 0:
			self.assertEqual(type(pd[0]), DictDna)


class TestListDna(TestCase):
	def test_dna_default_constructor(self):
		d = ListDna()
		self.assertNotEqual(ListDna(), None)
		self.assertEqual(type(d.data), list)
		self.assertEqual(len(d), d.default_initial_size)

	def test_int_in_dna(self):
		d = ListDna()
		if len(d) != 0:
			self.assertEqual(type(d[0]), int)

	def test_has_fitness_function_attribute(self):
		d = ListDna()
		self.assertNotEqual(d.fitness_function(), None)

	def test_fintess_function_default_dummy_implementation(self):
		"""test that by default fitness_function counts sum of genes in dna"""
		d = ListDna()
		self.assertEqual(d.fitness_function(), sum(d))


class TestCrossover(TestCase):
	def test_crossover_function_returns_two_dna_objects(self):
		d1 = ListDna()
		d2 = ListDna()
		d11, d12 = crossover(d1, d2)
		self.assertEqual(type(d11),ListDna)
		self.assertEqual(type(d12),ListDna)

	def test_crossover_with_one_crossing_point(self):
		d1 = ListDna([1, 1, 1, 1, 1])
		d2 = ListDna([0, 0, 0, 0, 0])
		d11, d12 = crossover(d1, d2, [3])
		self.assertEqual(d11.data, [1, 1, 1, 0, 0])
		self.assertEqual(d12.data, [0, 0, 0, 1, 1])


class TestDictDna(TestCase):
	"""test dict based dna with """
	def test_dict_dna_constructor(self):
		d = DictDna()
		self.assertNotEqual(DictDna(), None)
		self.assertEqual(type(d.data), dict)
		self.assertTrue(len(d) <= d.max_inital_size)

	def test_index_is_normalized(self):
		d = DictDna()
		for item in d:
			self.assertTrue(item <= 1)

	def test_initial_size_is_random(self):
		pass

# def print_dict(d):
# 	print('{', end="")
# 	for k, v in sorted(d.items()):

# 		print ( k, ':', v, ',', end="")
# 	print('}')

class TestLengthCrossover(TestCase):
	def test_different_length_crossover(self):
		d1 = DictDna({0.0 : 1 ,0.1 : 1 ,0.2 : 1 ,0.3 : 1 ,0.4 : 1 ,
			          0.5 : 1 ,0.6 : 1 ,0.7 : 1 ,0.8 : 1 ,0.9 : 1 })
		d2 = DictDna({0.0 : 0 ,0.2 : 0 ,0.4 : 0 ,0.6 : 0 ,0.8 : 0})
		start = 0.3
		end  = 0.7
		d11, d12 = different_length_crossover(d1, d2, start, end)
		self.assertEqual(d11, {0.0 : 1 ,0.1 : 1 ,0.2 : 1 ,0.3 : 1 ,0.4 : 0,
							   0.6 : 0 ,0.7 : 1 ,0.8 : 1 ,0.9 : 1})
		self.assertEqual(d12, {0.0 : 0 ,0.2 : 0 ,0.4 : 1 ,0.5 : 1 ,0.6 : 1 ,0.8 : 0})
		self.assertEqual(len(d1) + len(d2), len(d11) + len(d12))

	
if __name__ == '__main__':
	unittest.main()		

