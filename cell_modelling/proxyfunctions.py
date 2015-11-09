def add_succeeding_zeroes(max_number,number):
    string_number = str(number)
    string_number_length = len(string_number)
    wanted_string_number_length = len(str(max_number))
    string_number = '0'*(wanted_string_number_length-string_number_length)+string_number
    return string_number

def to_bin_string(max_number, number):
    return add_succeeding_zeroes(int('1'*max_number),(bin(number)[2:]) )

def bool_list_to_int(bool_list):
    s=""
    for item in bool_list:
        s+=str(item)
    return int("0b"+s,base=2)


#42-> 32+8+2 -> [1,0,1,0,1,0]
def decimal_int_to_binary_list(decimal_int):
    return list(bin(decimal_int)[2:])

def bool_list_to_string(lst):
    re_str=""
    for item in lst:
        re_str+=str(item)
    return re_str
