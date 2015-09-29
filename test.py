import unittest 

from population import Population
from dna import Dna, crossover

from unittest import TestCase


class TestPopulation(TestCase):
	def test_population_inits(self):
		p = Population()
		self.assertNotEqual(Population(), None)
		self.assertEqual(type(p.data), list)
		self.assertEqual(len(p), p.initial_size)

	def test_dna_in_population(self):
		p = Population()
		if len(p) != 0:
			self.assertEqual(type(p[0]), Dna)

class TestDna(TestCase):
	def test_dna_default_constructor(self):
		d = Dna()
		self.assertNotEqual(Dna(), None)
		self.assertEqual(type(d.data), list)
		self.assertEqual(len(d), d.default_initial_size)

	def test_int_in_dna(self):
		d = Dna()
		if len(d) != 0:
			self.assertEqual(type(d[0]), int)

	def test_has_fitness_function_attribute(self):
		d = Dna()
		self.assertNotEqual(d.fitness_function(), None)

	def test_fintess_function_default_dummy_implementation(self):
		"""test that by default fitness_function counts sum of genes in dna"""
		d = Dna()
		self.assertEqual(d.fitness_function(), sum(d))

class TestCrosover(TestCase):
	def test_crossover_function_returns_two_dna_objects(self):
		d1 = Dna()
		d2 = Dna()
		d11, d12 = crossover(d1, d2)
		self.assertEqual(type(d11),Dna)
		self.assertEqual(type(d12),Dna)

	def test_crossover_with_one_crossing_point(self):
		d1 = Dna([1, 1, 1, 1, 1])
		d2 = Dna([0, 0, 0, 0, 0])
		d11, d12 = crossover(d1, d2, [3])
		self.assertEqual(d11.data, [1, 1, 1, 0, 0])
		self.assertEqual(d12.data, [0, 0, 0, 1, 1])
		




		
		


	
if __name__ == '__main__':
	unittest.main()		

