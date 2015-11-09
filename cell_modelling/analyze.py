import saveload
from proxyfunctions import *
import os



def count_averarage_stability_and_cycle_amount(automata_list):
    stability_sum=0
    stability_square_sum=0
    cycle_amount_sum=0
    cycle_amount_square_sum=0
    automata_list_length=len(automata_list)

    for automata in automata_list:
        stability_sum+=automata.stability
        cycle_amount_sum+=automata.basin_amount

    average_stability=float(stability_sum)/automata_list_length
    average_cycle_amount=float(cycle_amount_sum)/automata_list_length

    for automata in automata_list:
        stability_square_sum+=(average_stability-automata.stability)**2
        cycle_amount_square_sum+=(average_cycle_amount-automata.basin_amount)**2
        #print automata.stability, automata.basin_amount

    stability_standard_error=math.sqrt(float(stability_square_sum)/automata_list_length)
    cycle_amount_standard_error=math.sqrt(float(cycle_amount_square_sum)/automata_list_length)



    print "Average stability:", str(average_stability)+"+-"+str(stability_standard_error*3)
    print "Average cycle_amount:", str(average_cycle_amount)+"+-"+str(cycle_amount_standard_error*3)


def stability_to_file(automata_list,current_folder_path):
    f=open(current_folder_path+"/" +"stat_file.txt",'w')
    for automata in automata_list:
        f.write(str(automata.stability)+"\n")
    f.close()

def stability_to_files(N,K,automata_list,save_path,sample_desired_length):
    i=0
    f=open(save_path +"/"+generate_stat_file_name(N,K,i)+".txt",'w')
    for automata_index in range(len(automata_list)):
        if (automata_index % sample_desired_length)==0:
            i+=1
            f.close()
            f=open(save_path +"/"+generate_stat_file_name(N,K,i)+".txt",'w')
        f.write(str(automata_list[automata_index].stability)+"\n")
    f.close()

def return_time_to_files(N,K,automata_list,save_path,sample_desired_length):
    i=0
    f=open(save_path +"/"+generate_stat_file_name(N,K,i)+".txt",'w')
    for automata_index in range(len(automata_list)):
        if (automata_index % sample_desired_length)==0:
            i+=1
            f.close()
            f=open(save_path +"/"+generate_stat_file_name(N,K,i)+".txt",'w')
        f.write(str(automata_list[automata_index].expected_return_time)+"\n")
    f.close()

def generate_stat_file_name(N,K,I):
    max_n_k=20
    max_i=200
    return "N_"+add_succeeding_zeroes(max_n_k,N)+"__k_"+add_succeeding_zeroes(max_n_k,K)+"__i_"+add_succeeding_zeroes(max_i,I)


def create_automata_stability_samples(N,K,current_folder_path,sample_length,samples_amount):
    automata_list=[]
    print "gather_data:"
    automata_type_folder_name=SaveLoad.generate_automata_type_folder_name(N,K)
    SaveLoad.gather_data(automata_list,current_folder_path+'/'+"SavedAutomata"+'/'+automata_type_folder_name)
    print "stats_to_file:"
    #count_averarage_stability_and_cycle_amount(automata_list)
    save_path=current_folder_path+"/"+"Statistics"+"/"+"Stability"+"/"+automata_type_folder_name
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    stability_to_files(N,K,automata_list,save_path,sample_length)

def create_automata_return_time_samples(N,K,current_folder_path,sample_length,samples_amount):
    automata_list=[]
    print "gather_data:"
    automata_type_folder_name=SaveLoad.generate_automata_type_folder_name(N,K)
    SaveLoad.gather_data(automata_list,current_folder_path+'/'+"SavedAutomata"+'/'+automata_type_folder_name)
    print "stats_to_file:"
    #count_averarage_stability_and_cycle_amount(automata_list)
    save_path=current_folder_path+"/"+"Statistics"+"/"+"ReturnTime"+"/"+automata_type_folder_name
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    return_time_to_files(N,K,automata_list,save_path,sample_length)

