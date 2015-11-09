import unittest 

from population import Population
from dna import Dna, ListDna, DictDna, NK_Dna
from gene import Gene, BoolGene, NK_Gene

from unittest import TestCase

from collections import UserList, UserDict

from cell_modelling.automata import NK_Automata
from cell_modelling.boolfunction import BoolFunction


class TestPopulation(TestCase):

	def test_population_default_constructor(self):
		p = Population()
		self.assertNotEqual(Population(), None)
		self.assertEqual(type(p.data), list)
		self.assertEqual(len(p), p.population_size)
		if len(p) != 0:
			self.assertEqual(type(p[0]), ListDna)

	def test_populaion_strict_dna_class_constructor(self):
		pl = Population(DnaClass=ListDna)
		if len(pl) != 0:
			self.assertEqual(type(pl[0]), ListDna)
		pd = Population(DnaClass=DictDna)
		if len(pd) != 0:
			self.assertEqual(type(pd[0]), DictDna)
		plb_3_4 = Population(DnaClass=ListDna, 
							 GeneClass=BoolGene,
							 population_size=3, 
							 dna_size=4)
		self.assertEqual(type(plb_3_4[0]), ListDna)
		self.assertEqual(type(plb_3_4[0][0]), BoolGene)
		self.assertEqual(len(plb_3_4),3)
		self.assertEqual(len(plb_3_4[0]),4)

	def test_population_step(self):
		p = Population()
		data_before = p.data[:]
		size_before = len(p)
		p.step()
		self.assertEqual(len(p.data), size_before)
		self.assertNotEqual(p.data, data_before)

	def test_itetate_with_dummy_fitness_functions(self):
		dna_size = 5

		p = Population(DnaClass=ListDna,
					   GeneClass=BoolGene,
					   population_size=1000,
					   dna_size=dna_size,
					   generations=1000)
		self.assertEqual(max([dna.fitness_function(dna) for dna in p]), dna_size)

		p = Population(DnaClass=DictDna,
					   GeneClass=BoolGene,
					   population_size=1000,
					   dna_size=dna_size,
					   generations=1000)
		self.assertEqual(max([dna.fitness_function(dna) for dna in p]), dna_size)
		

class TestListDna(TestCase):
	def test_dna_default_constructor(self):
		d = ListDna()
		self.assertEqual(type(d.data), list)
		self.assertTrue(isinstance(d, UserList)) # behaves like list
		if len(d) != 0:
			self.assertEqual(type(d.data[0]), BoolGene)
		self.assertEqual(len(d), d.default_dna_size)

	def test_dna_size_constructor(self):
		d = ListDna(dna_size=10)
		self.assertEqual(len(d), 10)
		self.assertEqual(type(d[0]), BoolGene)

	def test_dna_data_consrtuctor(self):
		d = ListDna(data=[True, False, True])
		self.assertEqual(len(d), 3)
		self.assertEqual(d[0].data, True)
		self.assertEqual(d[1].data, False)
		self.assertEqual(d[2].data, True)

	def test_has_fitness_default_function_attribute(self):
		"""test that by default fitness_function counts sum of True in dna"""
		d = ListDna(data=[True, False, True])
		self.assertNotEqual(d.fitness_function, None)
		self.assertEqual(d.fitness_function(d), 2)

	def test_crossover_returns_two_dna_objects(self):
		d1 = ListDna()
		d2 = ListDna()
		d11, d12 = ListDna.crossover(d1, d2)
		self.assertEqual(type(d11), ListDna)
		self.assertEqual(type(d12), ListDna)

	def test_crossover_with_one_crossing_point(self):
		d1 = ListDna(data=[1, 1, 1, 1, 1])
		d2 = ListDna(data=[0, 0, 0, 0, 0])
		d11, d12 = ListDna.crossover(d1, d2, [3])
		self.assertEqual([gene.data for gene in d11], [1, 1, 1, 0, 0])
		self.assertEqual([gene.data for gene in d12], [0, 0, 0, 1, 1])

	def test_crossover_on_itself(self):
		d = ListDna()
		d1, d2 = ListDna.crossover(d,d)
		self.assertEqual([gene.data for gene in d1],
					 	 [gene.data for gene in d2])


class TestDictDna(TestCase):
	"""test dict based dna with """
	def test_dict_dna_constructor(self):
		d = DictDna()
	
		# test DictDna behaves like dict
		self.assertEqual(type(d.data), dict)
		self.assertNotEqual(d.keys, None) 
		self.assertTrue(isinstance(d, UserDict))

		self.assertTrue(len(d) <= d.max_inital_size)

	def test_index_is_normalized(self):
		"""test dict keys are in range from 0 to 1"""
		d = DictDna()
		for item in d:
			self.assertTrue(item <= 1)

	def test_initial_size_is_random(self):
		pass

	def test_crossover(self):

		d1 = DictDna(data=[1,1,1,1,1,1,1,1,1,1])
		d2 = DictDna(data=[0,0,0,0,0])
		self.assertEqual(str(d1), "{0.0: 1, 0.1: 1, 0.5: 1, 0.7: 1, 0.9: 1, 0.3: 1, 0.8: 1, 0.2: 1, 0.4: 1, 0.6: 1}")
		self.assertEqual(str(d2), "{0.0: 0, 0.2: 0, 0.4: 0, 0.8: 0, 0.6: 0}")
		start = 0.3
		end  = 0.7
		d11, d12 = DictDna.crossover(d1, d2, start, end)
		self.assertEqual(str(d11),"{0.0: 1, 0.1: 1, 0.3: 1, 0.6: 0, 0.8: 1, 0.7: 1, 0.2: 1, 0.4: 0, 0.9: 1}")
		self.assertEqual(str(d12),"{0.0: 0, 0.2: 0, 0.6: 1, 0.8: 0, 0.4: 1, 0.5: 1}")
		self.assertEqual(type(d11), DictDna)
		self.assertEqual(type(d12), DictDna)

		# self.assertEqual(d11, {0.0 : 1 ,0.1 : 1 ,0.2 : 1 ,0.3 : 1 ,0.4 : 0,
		# 					   0.6 : 0 ,0.7 : 1 ,0.8 : 1 ,0.9 : 1})
		# self.assertEqual(d12, {0.0 : 0 ,0.2 : 0 ,0.4 : 1 ,0.5 : 1 ,0.6 : 1 ,0.8 : 0})
		self.assertEqual(len(d1) + len(d2), len(d11) + len(d12))


class TestNK_Dna(TestCase):
	def test_constructor_from_nk_automata(self):
		N = 4
		K = 3
		functions_list = [BoolFunction(K=K, values_string="01000000"),
						  BoolFunction(K=K, values_string="00100000"), 
						  BoolFunction(K=K, values_string="01000000"), 
						  BoolFunction(K=K, values_string="00100000"), 
						 ]
		automata = NK_Automata(N=N,
							   K=K,
							   functions_list=functions_list,
							   links_list=[[0, 1, 2],
							   			   [0, 1, 2],
							   			   [0, 1, 2],
							   			   [1, 2, 3]])
		automata.fill_automata()

		nk_dna = NK_Dna(automata)
		self.assertEqual(type(nk_dna), NK_Dna)
		self.assertTrue(isinstance(nk_dna, DictDna))
		self.assertEqual(nk_dna.GeneClass, NK_Gene)

		self.assertEqual(len(automata.functions_list), len(nk_dna))
		self.assertEqual(type(nk_dna[0.0]), NK_Gene)

		self.assertEqual(nk_dna.fitness_function(nk_dna), automata.stability)



class TestGene(TestCase):
	def test_bool_gene_default_constructor(self):
		g = BoolGene()
		self.assertEqual(g.data, False)

	def test_bool_gene_pain_data_constructor(self):
		g = BoolGene(True)
		self.assertEqual(g.data, True)

	def test_bool_gene_copy_constructor(self):
		g = BoolGene(True)
		c_copy = BoolGene(g)
		self.assertEqual(c_copy.data, True)

		# test copy does not depend on original
		g.data = False
		self.assertEqual(c_copy.data, True)

	def test_bool_gene_mutation(self):
		g = BoolGene()
		self.assertFalse(g.data)
		g.mute()
		self.assertTrue(g.data)

		g = BoolGene(True)
		self.assertTrue(g.data)
		g.mute()
		self.assertFalse(g.data)

class TestNK_Gene(TestCase):
	def 

	
if __name__ == '__main__':
	unittest.main()		


