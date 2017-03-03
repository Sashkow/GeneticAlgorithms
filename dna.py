from collections import UserList, UserDict

from gene import BoolGene, NK_Gene, LetterGene

from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

import copy

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


def letter_dna_fitness_function(letter_dna):
    return 200 - mt.Tm_NN(Seq(letter_dna.to_string()))




def seq_fitness_function(seqlist_dna):
    """
    1 point penalty for each nucleotide in intervals that are longer
    than min_interval_length; normaized to -1;

    [0,0,0..,all] -> all - min_interval_length
    """
    data = seqlist_dna.data
    seq_len = len(seqlist_dna.sequence)
    min_interval_length = seqlist_dna.min_interval_length

    lengths = [data[i] - data[i-1] for i in range(1, len(data))]
    lengths = [data[0]] + lengths + [seq_len - seqlist_dna[-1]]
    assert(len(seqlist_dna) + 1 == len(lengths))

    penalty = 0
    # when intervals "want" equal lengths equal to min length but
    # there is not enough sequence length for that
    supposed_penalty = (len(lengths) * min_interval_length) - seq_len
    if supposed_penalty > 0:
        min_penalty = supposed_penalty
    else:
        min_penalty = 0
    # when one interval has max length and all others are zeroes
    max_penalty = min_interval_length * (len(lengths) - 1) 

    for item in lengths:
        if item < min_interval_length:
            penalty += min_interval_length - item
    # print(min_penalty, penalty, max_penalty)
    # normaize to -1
    penalty = -((penalty - min_penalty) / (max_penalty - min_penalty))

    return penalty


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
        
        self._dna_size = ListDna.default_dna_size
        self.data = [GeneClass.generate_random() 
                 for i in range(self._dna_size)]    

        if "dna_size" in kwargs:
            self._dna_size = kwargs["dna_size"]
            self.data = [GeneClass.generate_random() 
                     for i in range(self._dna_size)]    

        if "data" in kwargs:
            self.data = list([GeneClass(item) for item in kwargs["data"]])


        if "fitness_function" in kwargs:
            self.fitness_function = kwargs["fitness_function"]
        else:
            self.fitness_function = dummy_fitness_function_for_list_dna

    def __str__(self):
        return ''.join([str(item) for item in self.data])

    
    def mute(self, mutation_probability):
        for gene in self:
            if random.random() < mutation_probability:
                print("muta!")
                gene.mute()

    def crossover(self, second_dna, cross_lst=[]):
        """
        a -- Dna object
        b -- Dna object
        cross_lst  -- list of points of crossover

        a and b should be of the same length

        return genetic recombination of two DNA's
        """
        if cross_lst == []:
            cross_lst = [random.randrange(len(self))]

        poc = cross_lst[0]
        temp = copy.deepcopy(self.data[poc:])
        self.data[poc:] = copy.deepcopy(second_dna.data[poc:])
        second_dna.data[poc:]=copy.deepcopy(temp)


class LetterListDna(ListDna):
    def __init__(self, GeneClass=BoolGene, **kwargs):
        """
        """
        kwargs.update({'GeneClass':LetterGene})
        super().__init__(**kwargs)

    def to_string(self):
        letters_lst = [str(letter) for letter in self.data]
        return ''.join(letters_lst)



class SeqListDna(Dna, UserList):
    """
    Constant sized DNA sequence in a genetic algorithm

    Represents intervals that split some biological sequence `seq`
    [0,2,2,4], AAGTAAA --> |AA||GT|AAA, nterval length are [0, 2, 0, 2, 3]
    """
    default_dna_size = 10
    default_min_interval_length = 5
    def __init__(self, seq="AAGTAAA", **kwargs):
        """
        args:
            seq - biological dna sequence string
        optional arguments:
            size -- amount of genes in dna
            data -- plain list of Gene objects or 
                    of plain data if GeneClass is can change types
            if both of these optional arguments are set then size is ignored

            fitness_function -- fitness function
        """
        super().__init__()
        self.fitness_function = seq_fitness_function
        self.sequence = seq

        if "size" in kwargs:
            self.size = kwargs["size"]
        else:
            self.size = SeqListDna.default_dna_size

        if "min_interval_length" in kwargs:
            self.min_interval_length = \
                    kwargs["min_interval_length"]
        else:
            self.min_interval_length = SeqListDna.default_min_interval_length



        if "data" in kwargs:
            self.size = len(kwargs["data"])
            self.data = kwargs["data"]
        else:
            self.data = [random.randrange(0,len(seq)) for i in range(self.size)]    
            self.data = sorted(self.data)


        # if len(kwargs) == 0:
        #   self.sequence = seq
            
        #   self.data = [random.randrange(0,len(seq)) for i in range(self._dna_size)]   
        #   self.data = sorted(self.data)

        # self._dna_size = self.default_dna_size
        # if "dna_size" in kwargs:
        #   self._dna_size = kwargs["dna_size"]
        #   self.data = [GeneClass.generate_random() 
        #            for i in range(self._dna_size)]    

        # if "data" in kwargs:
        #   self.data = list([GeneClass(item) for item in kwargs["data"]])

        # self.fitness_function = dummy_fitness_function_for_list_dna

    
    def mute(self, mutation_probability):
        #for gene in dna
        for i in range(len(self.data)):
            if random.random() > .01:
                if i == 0:

                    new_gene = random.randrange(0, self[i+1]+1)
                elif i == len(self.data) - 1:
                    new_gene = random.randrange(self[i-1],len(self.data)+1)
                else:
                    new_gene = random.randrange(self[i-1],self[i+1]+1)
                self.data[i] = new_gene

    @staticmethod
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
        s1 = SeqListDna(data=a[:poc] + b[poc:])
        s1.data = sorted(s1.data)
        s2 = SeqListDna(data=b[:poc] + a[poc:])
        s2.data = sorted(s2.data)
        return s1, s2






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
        #   _dna_size = random.randrange(1, DictDna.max_inital_size + 1)
        #   self.data = dict({(float(i)/(_dna_size)):
        #                      GeneClass.generate_random() 
        #                      for i in range(_dna_size)})  
        

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
                print("muta")
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
        assert(type(self.data) == dict)
        
        self.GeneClass = NK_Gene
        self.automata = automata

        self.fitness_function = dummy_fitness_function_for_nk_dna
