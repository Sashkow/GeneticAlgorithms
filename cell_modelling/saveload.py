
import sys
import os
import pickle
import shutil
import os.path

def save_variable_to_file(variable,file_name,file_path):
    a_file=open(file_path+'/'+file_name,'w')
    pickle.dump(variable,a_file)
    a_file.close()

def load_variable_from_file(file_name,file_path):
    a_file=open(file_path+'/'+file_name,'r')
    variable = pickle.load(a_file)
    a_file.close()
    return variable

import sys
import os
import pickle
import shutil
from cell_modelling.proxyfunctions import*


def save_variable_to_file(variable,file_name,file_path):
    a_file=open(file_path+'/'+file_name,'w')
    pickle.dump(variable,a_file)
    a_file.close()

def load_variable_from_file(file_name,file_path):
    a_file=open(file_path+'/'+file_name,'r')
    #print file_path+'/'+file_name
    variable = pickle.load(a_file)
    a_file.close()
    return variable

def generate_automata_type_folder_name(N,K):
    max_n_k=20
    return "N_"+add_succeeding_zeroes(max_n_k,N)+"__k_"+add_succeeding_zeroes(max_n_k,K)

def generate_automata_folder_name(automata_type_folders_collection):
    max_automata_folders_amount=999
    current_automat_folders_amount=len(automata_type_folders_collection)
    return add_succeeding_zeroes(max_automata_folders_amount,current_automat_folders_amount)

def save_n_k_automata(current_folder_path,nk_automata,picture=False):

    data_folder_path = os.path.join(current_folder_path, '../../data')

    automata_types_folder_path=os.path.join(data_folder_path,'SavedAutomata')

    if not os.path.exists(automata_types_folder_path):
        os.makedirs(automata_types_folder_path)


    automata_types_folder_collection = os.listdir(automata_types_folder_path)

    automata_type_folder_name = generate_automata_type_folder_name(nk_automata.N,nk_automata.K)

    automata_type_folder_path = automata_types_folder_path+'/'+automata_type_folder_name

    if not os.path.exists(automata_type_folder_path):
        os.makedirs(automata_type_folder_path)

    automata_folders_collection = os.listdir(automata_type_folder_path)

    #folders are numbered '000','001','002'...
    automata_folder_name = generate_automata_folder_name(automata_folders_collection)

    automata_folder_path = automata_type_folder_path+'/'+automata_folder_name

    os.makedirs(automata_folder_path)

    #print automata_folder_path

    save_variable_to_file(nk_automata,'automata.txt',automata_folder_path)

    if picture:
        graph_file_name = automata_type_folder_name+'_'+automata_folder_name+'.png'
        graph_cycles_only_file_name = automata_type_folder_name+'_'+automata_folder_name+"__cycles_only"+'.png'
        graph_fun_links_file_name = automata_type_folder_name+'_'+automata_folder_name+"__fun_links"+'.png'

        if os.path.exists(current_folder_path+'/'+'temp_pic.png'):
            shutil.copyfile(current_folder_path+'/'+'temp_pic.png', os.path.join(data_folder_path, graph_file_name))
        if os.path.exists(data_folder_path+'/'+'temp_pic2.png'):
            shutil.copyfile(data_folder_path+'/'+'temp_pic2.png', os.path.join(automata_folder_path,graph_cycles_only_file_name))
        if os.path.exists(data_folder_path+'/'+'temp_pic3.png'):
            shutil.copyfile(data_folder_path+'/'+'temp_pic3.png', os.path.join(automata_folder_path, graph_fun_links_file_name))


def gather_data(automata_list,automata_folders_folder_path):
    automata_folders_list=os.listdir(automata_folders_folder_path) #'000','001','002'
    i=0
    for automata_folder_name in automata_folders_list:
        print("gathering:", i)
        i+=1
        nk_automata=load_variable_from_file('automata.txt',automata_folders_folder_path+'/'+automata_folder_name)
        automata_list.append(nk_automata)


def test_folders_creation(data_folder_path):
    automata=[]
    enters=[]
    initial_state=[]
    N=5
    K=5
    I=3
    for n in range(N):
        for k in range(K):
            for i in range(I):
                save_n_k_automata(automata,enters,initial_state,data_folder_path,n,k)
