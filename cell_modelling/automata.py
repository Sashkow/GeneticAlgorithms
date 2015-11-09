import cell_modelling.generate_automata
from cell_modelling.boolfunction import BoolFunction
import cell_modelling.state

import sys
import cell_modelling.drawgraph


from cell_modelling.debug import log
from cell_modelling.state import State

import random

class NK_Automata(object):
    graph_names_list = ['gene_links_graph','cell_states_graph','simplified_cell_states_graph']
    
    def __init__(self,
                 N=None,
                 K=None,
                 functions_list=None,
                 links_list=None,
                 view_states_as_binary=False):
        if N==None or K==None:
            self.N = 5
            self.K = 5
        else:
            self.N = N
            self.K = K

        # share of zeroes in boolean functions' values
        self.zeroes = .5

        if functions_list == None:
            self.functions_list = []
        else:
            self.functions_list = functions_list

        if links_list == None:
            self.links_list = []
        else:
            self.links_list = links_list

        self.ordinal_number = -1

        
        self.state_span = {}              #state_span: {current_state_number: next_state_number,...}
        self.state_list = []           
        self.attractor_dict = {}          #attractor_dict {attractor_number:[size,basin_size],...}
        self.attractor_states_dict = {}   #attractor_states_dict: {attractor_state_number:[next_attractor_state_number,attractor_state_weight],...} 

        self.basin_amount = 0
        self.stability = 0 

        self.expected_return_time = 9000

        self.view_states_as_binary =view_states_as_binary

        

    def __sizeof__(self):
        return sys.getsizeof(self.N) + sys.getsizeof(self.K) + \
               sys.getsizeof(self.functions_list) + \
               sys.getsizeof(self.links_list) + sys.getsizeof(self.state_span) + \
               sys.getsizeof(self.basin_amount) + sys.getsizeof(self.stability) + \
               sys.getsizeof(self.attractor_dict)

    def __str__(self):
        #return "N = " + str(self.N)+ " K = " + str(self.K) +"\n"+"functions_list: "+str(self.functions_list)+"\n"+"links_list: " + str(self.links_list)
        return "N = " + str(self.N)+ " K = " + str(self.K) + \
               "functions_list: " + str(self.functions_list) + \
               "links_list: " + str(self.links_list)

    def __repr__(self):
        return self.__str__()

    """
    zeroes - share of zeroes in boolean functions' values
    """
    def generate_random_automata(self):
        self.functions_list=[]
        self.links_list=[]
        generate_automata.generate_n_k_automata(self.N, self.K,
            self.functions_list, self.links_list, self.zeroes)

    def step_automata(self,state):
        new_state_string=""
        for bool_fun_number in range(self.N):

            bool_fun_inputs=""
            for state_element_number in range(self.K):
                bool_fun_inputs += \
                    state.as_string()[self.links_list[bool_fun_number][state_element_number]]

            new_state_string+=self.functions_list[bool_fun_number].evaluate(bool_fun_inputs)

        return State(new_state_string)


    def span_automata(self):
        if self.state_span:
            self.state_span={}

        #print "Iterating automata states:"
        current_state=State(0,self.N)
        next_state=State(0,self.N)
        for state_number in range(2**self.N):


            #print "Current state:", state_number
            current_state.set_state(state_number)

            next_state=self.step_automata(current_state)

            if self.view_states_as_binary:
                self.state_span[current_state.as_string()[::]]=next_state.as_string()[::]
            else:
                self.state_span[current_state.as_int()]=next_state.as_int()
            

    def create_state_list(self):
        for state_number in range(2**self.N):
            self.state_list.append(State(state_number,self.N))
#
    def process_sample(self,seed):
        current_state_number=seed
        sample_list=[]
        while not (current_state_number in sample_list):

            if self.state_list[current_state_number].in_attractor:

                for sample_state_number in sample_list:
                    self.state_list[sample_state_number].in_basin=True
                    self.state_list[sample_state_number].basin_number=self.state_list[current_state_number].basin_number
                    self.state_list[sample_state_number].first_attractor_state_number=current_state_number
                self.state_list[current_state_number].weight+=len(sample_list)
                return

            if self.state_list[current_state_number].in_basin:
                first_attractor_state_number = self.state_list[current_state_number].first_attractor_state_number
                for sample_state_number in sample_list:
                    self.state_list[sample_state_number].in_basin=True
                    self.state_list[sample_state_number].basin_number=self.state_list[current_state_number].basin_number
                    self.state_list[sample_state_number].first_attractor_state_number=first_attractor_state_number
                self.state_list[first_attractor_state_number].weight+=len(sample_list)
                return

            sample_list.append(current_state_number)
            current_state_number=(self.step_automata(State(current_state_number,self.N))).as_int()


        attractor_start_state_number=current_state_number

        attractor_start_index=sample_list.index(attractor_start_state_number)
        basin_list=sample_list[:attractor_start_index]
        attractor_list=sample_list[attractor_start_index:]

        for state_number in basin_list:
            self.state_list[state_number].in_basin=True
            self.state_list[state_number].basin_number=self.basin_amount+1
            self.state_list[state_number].first_attractor_state_number=attractor_start_state_number

        for state_number in attractor_list:
            self.state_list[state_number].in_attractor=True
            self.state_list[state_number].basin_number=self.basin_amount+1

        self.state_list[attractor_start_state_number].weight=len(basin_list)

        self.basin_amount+=1
    ###

    #next state object

    def next_state(self,state):
        next_state_string=self.state_span[state.as_string()]
        next_state_number=State(next_state_string).state_number
        next_state_object=self.state_list[next_state_number]
        return next_state_object
    ###

    def analyse_automata(self):
        #print "starting analysis:"
        self.create_state_list()
        sample_number=0
        for state_number in range(2**self.N):
            if self.state_list[state_number].in_basin==False and self.state_list[state_number].in_attractor==False:
                #print "  taking_sample:", sample_number
                self.process_sample(state_number)
            sample_number+=1

    def initialize_attractor_dict(self):
        for attractor_number in range(1,self.basin_amount+1):
            self.attractor_dict[attractor_number]=[0,0] # {attractor_number:[size,basin_size],...}

    def make_attractor_stat_dictionary(self):
        
        self.initialize_attractor_dict()
        for state in self.state_list:
            if state.in_attractor==True:
                self.attractor_dict[state.basin_number][0]+=1
            if state.in_basin==True:
                self.attractor_dict[state.basin_number][1]+=1

    def count_stability(self):
        basin_size_square_sum = 0
        for attractor_number in self.attractor_dict:
            basin_size_square_sum += (self.attractor_dict[attractor_number][0] + self.attractor_dict[attractor_number][1])**2
        self.stability=float(basin_size_square_sum)/(2**(self.N))**2 
        return self.stability

    """
    count experimental probability of staying in the same basin after a random
    perturbation
    """
    def count_stability_experimental(self):
        perturbations= 1000
        stay = 0
        for i in range(perturbations):
            random_state = random.randrange(2**self.N)
            old_basin = self.state_list[random_state].basin_number
            random_state= random.randrange(2**self.N)
            new_basin= self.state_list[random_state].basin_number
            if new_basin == old_basin:
                stay += 1
        return stay / float(perturbations)


    """
    count probability to stay in the same basin after minimal perturbation 
    on contition of being in certain state
    """
    def p_stay_in_basin(self, state):
        basin_number = state.basin_number
        basin_size = self.attractor_dict[basin_number][1]
        state_number = state.state_number
        state_str = state.as_string()

        stay_cases = 0
        perturbations_amount = len(state_str)
        for i in range(perturbations_amount):
            inverted_bit = str(1 - int(state_str[i]))
            perverted_state_str = state_str[:i] + inverted_bit + state_str[i+1:]
            perverted_state = State(perverted_state_str)

            if self.state_list[perverted_state.state_number].basin_number == \
              basin_number:
                stay_cases += 1

        return stay_cases / float(perturbations_amount)

    def count_stability_minimal(self):
        stability = 0
        p_appear_in_state = float(1)/2**self.N
        for state in self.state_list:
            stability += self.p_stay_in_basin(state) * p_appear_in_state
        return stability

    def count_stability_minimal_experimental(self):
        perturbations= 1000
        stay = 0
        for i in range(perturbations):
            random_state = random.randrange(2**self.N)
            old_basin = self.state_list[random_state].basin_number
            random_bit= random.randrange(self.N)
            #flip random bit of a state
            random_state = random_state ^ (1 << random.randrange(self.N))
            new_basin= self.state_list[random_state].basin_number
            if new_basin == old_basin:
                stay += 1
        return stay / float(perturbations)



    def distance_between_states(self,from_state,to_state):

        current_state=from_state
        distance = 0
        while current_state!=to_state:
            distance+=1
            current_state=self.next_state(current_state)

           # print "      CurrentState:", current_state
            if distance>100500:
                print("err")
                return -1
        #print "FromState:", from_state, "ToState:", to_state, "distance:", distance

        return distance


    def count_expected_return_time(self):
        # average timesteps needed to reach some cycle in case of random state change i.e. average distance to the nearest cycle
        average_return_time = 0
        basin_states_amount = 0
        for current_state in self.state_list:

            if current_state.in_basin==True:
                basin_states_amount+=1
                first_attractor_state=self.state_list[current_state.first_attractor_state_number]

                average_return_time+=self.distance_between_states(current_state,first_attractor_state)
        if basin_states_amount==0:
            self.expected_return_time=0
            return 0
        average_return_time=float(average_return_time)/basin_states_amount
        self.expected_return_time=average_return_time
        return average_return_time

    def make_attractor_states_dictionary(self):
        self.attractor_states_dict={}
        for state in self.state_list:
            if state.in_attractor==True:
                if self.view_states_as_binary:
                    self.attractor_states_dict[state.as_string()]=[(self.step_automata(state)).as_string(),state.weight]
                else:
                    self.attractor_states_dict[state.as_int()]=[(self.step_automata(state)).as_int(),state.weight]
        
    def fill_automata(self):

        # self.generate_random_automata()
        # # print "automata", self

        self.span_automata()
        # print "satespan",self.state_span

        self.analyse_automata()
        # print self.state_list

        self.make_attractor_states_dictionary()
        # print "attractor states:", self.attractor_states_dict

        self.make_attractor_stat_dictionary()

        self.count_stability()

def find_element_in_list(element,list_element):
        try:
            index_element=list_element.index(element)
            return index_element
        except ValueError:
            return -1
"""
create a new automata with one of it's variables doubled
"""
def duplicate_random_gene(nk_automata):

    """copy existing automata"""
    new_automata = NK_Automata(nk_automata.N+1,
                                 nk_automata.K+1,
                                 nk_automata.functions_list,
                                 nk_automata.links_list,
                                 nk_automata.view_states_as_binary)
    """pick gene to duplicate"""
    gene_to_copy = 0 #random.randrange(N)
    """add copied function and input genes list"""
    new_automata.functions_list.append(nk_automata.functions_list[gene_to_copy])
    new_automata.links_list.append(nk_automata.links_list[gene_to_copy])
    copied_gene = len(new_automata.links_list) - 1 #copied gene is in the end of the list

    """if gene_to_copy influences any other gene, the copied_gene should also
       influence that gene via OR rule"""
    new_functions_list = []
    new_links_list = []
    for gene_index, links in enumerate(new_automata.links_list):    
        indexof_gene_to_copy = find_element_in_list(gene_to_copy, links)
        # print gene_index, links
        new_links_list.append(new_automata.links_list[gene_index]+[copied_gene])
        new_bool_function_values = ""
        for i in range(2**(new_automata.K)):
            i_bin_str = bin(i)[2:]
            inputs_string ='0'*(new_automata.K - len(i_bin_str)) + i_bin_str
            if indexof_gene_to_copy != -1:
                copied_gene_value = inputs_string[-1]
                gene_to_copy_value = inputs_string[indexof_gene_to_copy]
                gene_to_copy_value = bin(int(gene_to_copy_value) or int(copied_gene_value))[2:]
                inputs_string = inputs_string[:indexof_gene_to_copy] + gene_to_copy_value + inputs_string[indexof_gene_to_copy+1:]

            new_bool_function_values += \
              new_automata.functions_list[gene_index].evaluate(inputs_string[:-1])

        new_bool_function = BoolFunction(new_automata.K, new_bool_function_values)
        new_functions_list.append(new_bool_function)
        
    new_automata.functions_list = new_functions_list
    new_automata.links_list = new_links_list

    return new_automata





def main():
    #(2)<-(0)<->(1) 
    # N = 3 K = 2 functions_list: [0000, 1101, 0001]links_list: [[0, 1], [1, 0], [0, 2]]
    import pickle
    a = NK_Automata(6,6)    
    # a.fill_automata()
    # pickle.dump(a, open('temp_automata.txt','w'))
    # a = pickle.load(open('temp_automata.txt','r'))
    a.view_states_as_binary = True
    a.fill_automata()

    # print a 
    # print a.state_span
    # print a.state_list
    # print a.attractor_dict
    # print a.count_stability()
    # print a.count_stability_minimal()
    # import drawgraph
    # dg = drawgraph.DrawGraph(a)
    # dg.gene_links_graph()
    # dg.cell_states_graph()

if __name__ == '__main__':
    main()