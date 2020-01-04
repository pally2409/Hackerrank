#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    m = min(len(a), len(b))
    l = []
    lena = len(a)
    lenb = len(b)
    if(m == len(a)):
        for i in range(len(a)):
            if a[i] in b:
                c = b.index(a[i])
                b = b[:c] + b[(c+1):]
                l.append(a[i])
    else:
        for i in range(len(b)):
            if b[i] in a:
                c = a.index(b[i])
                a = a[:c] + a[(c+1):]
                l.append(b[i])
    result = (lena - len(l)) + (lenb - len(l))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

