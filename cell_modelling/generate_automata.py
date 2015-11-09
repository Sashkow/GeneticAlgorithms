
from cell_modelling.proxyfunctions import*
import cell_modelling.boolfunction
import random

"""
zeroes - float from 0 to 1. Share of zeroes in functions values.
"""
def generate_n_k_automata(N,K,functions_list,links_list, zeroes):
    generate_functions_list(N,K,functions_list, zeroes)
    generate_links_list(N,K,links_list)
    #generate_state(initial_state,N)



def generate_functions_list(N,K,functions_list, zeroes):    
    for i in range(N):
        #print "generating function", i
        bf = boolfunction.BoolFunction(K)
        bf.generate_random(zeroes)
        functions_list.append(bf)



def generate_links_list(N,K,links_list):
    for n in range(N):
        lst = range(N)
        random.shuffle(lst)
        links_list.append(lst[:K])
        
