import os, sys
lib_path = os.path.abspath('')
sys.path.append(lib_path)
print lib_path


from automata import NK_Automata
from debug import log

from state import State 
import analyze
from boolfunction import*
from proxyfunctions import*
from drawgraph import DrawGraph
 
import saveload

import os
   #N=4 K=2 8257536 
def do_automata(N,K,nk_automata=None,ordinal_number=-1):
    draw_graph_object = DrawGraph()

    current_folder_path = os.path.dirname(__file__)
    
    if nk_automata == None:
        nk_automata = NK_Automata(N, K)
        nk_automata.generate_random_automata()
    
    nk_automata.ordinal_number = ordinal_number
    print nk_automata
    
    nk_automata.span_automata()
    print "satespan",nk_automata.state_span
    
    nk_automata.analyse_automata()
    print nk_automata.state_list
    
    nk_automata.make_attractor_stat_dictionary()
    print nk_automata.attractor_dict
    
    nk_automata.count_stability()
    print "Stability:", nk_automata.stability
    
    nk_automata.count_expected_return_time()
    print "ExpectedReturnTime:", nk_automata.expected_return_time

    draw_graph_object.draw_gene_connecions_graph(nk_automata.links_list, current_folder_path)
    
    draw_graph_object.draw_states_graph(nk_automata.state_span, current_folder_path)

    draw_graph_object.draw_simplfied_states_graph(nk_automata.attractor_dict,2**nk_automata.N,current_folder_path)

    # print "saving..."
    # saveload.save_n_k_automata(current_folder_path, nk_automata, True)
    # print "saved."
