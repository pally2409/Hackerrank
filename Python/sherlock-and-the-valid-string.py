#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    init_dict = {}
    
    for i in range(len(s)):
        if s[i] in init_dict.keys():
            init_dict[s[i]] = init_dict[s[i]] + 1
        else:
            init_dict[s[i]] = 1
    print(init_dict)
    set_init_dict = set(init_dict.values())
    print(set_init_dict)
    if len(set_init_dict) == 1:
        print('here1')
        return 'YES'
    else:
        dict_of_freq = {}
        list_of_val = list(init_dict.values())
        print('init dict vals')
        print(init_dict.values())
        for i in range(len(list_of_val)):
            if list_of_val[i] in dict_of_freq.keys():
                dict_of_freq[list_of_val[i]] = dict_of_freq[list_of_val[i]] + 1
            else: 
                dict_of_freq[list_of_val[i]] = 1
        if len(dict_of_freq.values()) == 2:
            dict_of_freq_keys = list(dict_of_freq.keys())
            dict_of_freq_values = list(dict_of_freq.values())
            if min(dict_of_freq.values()) == 1:
                if dict_of_freq_values[0] == 1:
                    if dict_of_freq_keys[0] - 1 == dict_of_freq_keys[1] or dict_of_freq_keys[0] - 1 == 0:
                        print('here2')
                        return 'YES'
                    else:
                        return 'NO'
                else:
                    if dict_of_freq_keys[1] - 1 == dict_of_freq_keys[0] or dict_of_freq_keys[1] - 1 == 0:
                        print('here3')
                        print(dict_of_freq_keys)
                        return 'YES'
                    else:
                        return 'NO'
            else:
                return 'NO'
        else:
            return 'NO'
                 
                
    







    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

