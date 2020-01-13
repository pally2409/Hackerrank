#!/bin/python3

import math
import os
import random
import re
import sys
import queue


# Complete the isBalanced function below.

def isBalanced(s):
    lis_s = []
    dict_sym = {}
    dict_sym['('] = ')'
    dict_sym['{'] = '}'
    dict_sym['['] = ']'
    for i in range(len(s)):
        if s[i] in dict_sym.keys():
            lis_s.append(s[i])
        else:
            if len(lis_s)!=0:
                popped = lis_s.pop()
                if dict_sym[popped] != s[i]:
                    return 'NO'
            else:
                return 'NO'
    if len(lis_s) == 0:
        return 'YES'
    else:
        return 'NO'
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

