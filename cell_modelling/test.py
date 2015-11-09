# import Automata
# import BoolFunction
# import AutomataProssesing
# ### has_basin_level_bijections testing begin
# #returns two automatas with same basin sizes but different attractor sizes 
# def basin_attractors_do_not_match_trigger_automatas():
#     N=3
#     K=3
    
#     functions_list1=[]
#     functions_list1.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000001"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000000"))
    
#     links_list1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
#     automata1 = Automata.NK_Automata(N,K,functions_list1,links_list1)
    
#     AutomataProssesing.do_automata(N,K,automata1)
    
#     functions_list2=[]
#     functions_list2.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"01000110"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"00001010"))
    
#     links_list2=[[0,1,2],[0,1,2],[0,1,2]]
    
#     automata2 = Automata.NK_Automata(N,K,functions_list2,links_list2)
    
#     AutomataProssesing.do_automata(N,K,automata2)
    
#     return automata1,automata2

# def basin_attractor_of_certain_size_is_absent_trigger_automatas():
#     N=3
#     K=3
    
#     functions_list1=[]
#     functions_list1.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000001"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000000"))
    
#     links_list1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
#     automata1 = Automata.NK_Automata(N,K,functions_list1,links_list1)
    
#     AutomataProssesing.do_automata(N,K,automata1)
    
#     functions_list2=[]
#     functions_list2.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"01000110"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"10001010"))
    
#     links_list2=[[0,1,2],[0,1,2],[0,1,2]]
    
#     automata2 = Automata.NK_Automata(N,K,functions_list2,links_list2)
    
#     AutomataProssesing.do_automata(N,K,automata2)
    
#     return automata1,automata2

# #automatas of equal amount of basins and attractor and basin sizes but different structure.
# def brute_force_beginning_trigger_automatas():
#     N=3
#     K=3
    
#     functions_list1=[]
#     functions_list1.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000001"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00000000"))
    
#     links_list1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
#     automata1 = Automata.NK_Automata(N,K,functions_list1,links_list1)
    
#     AutomataProssesing.do_automata(N,K,automata1)
    
#     functions_list2=[]
#     functions_list2.append(BoolFunction.BoolFunction(K,"00001111"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"01000110"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"00000010"))
    
#     links_list2=[[0,1,2],[0,1,2],[0,1,2]]
    
#     automata2 = Automata.NK_Automata(N,K,functions_list2,links_list2)
    
#     AutomataProssesing.do_automata(N,K,automata2)
    
#     return automata1,automata2

# def brute_force_beginning_trigger_after_simple_bijection_trigger_automatas():
#     N=3
#     K=3
    
#     functions_list1=[]
#     functions_list1.append(BoolFunction.BoolFunction(K,"00001110"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"01000000"))
#     functions_list1.append(BoolFunction.BoolFunction(K,"00100000"))
    
#     links_list1=[[0,1,2],[0,1,2],[0,1,2]]
     
#     automata1 = Automata.NK_Automata(N,K,functions_list1,links_list1)
    
#     AutomataProssesing.do_automata(N,K,automata1)
    
#     functions_list2=[]
#     functions_list2.append(BoolFunction.BoolFunction(K,"01001111"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"00000100"))
#     functions_list2.append(BoolFunction.BoolFunction(K,"00000010"))
    
#     links_list2=[[0,1,2],[0,1,2],[0,1,2]]
    
#     automata2 = Automata.NK_Automata(N,K,functions_list2,links_list2)
    
#     AutomataProssesing.do_automata(N,K,automata2)
    
#     return automata1,automata2

# ### has_basin_level_bijections testing end
# def my_append(element,lst=[]):
#     lst.append(element)
#     return lst


    
    
    
# if __name__ == '__main__':
#   main() 
  
#    