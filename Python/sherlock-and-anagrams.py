#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    signatures = {}
    result = 0
    for i in range(len(s)):
        wor = ''
        for j in range(i, len(s), 1):
            signature = [0]*26
            wor = wor + s[j]
            for letter in wor:
                signature[ord(letter) - ord('a')] = signature[ord(letter) - ord('a')] + 1
            signature = tuple(signature)
            if signature in signatures.keys():
                signatures[signature] = signatures[signature] + 1
            else:
                signatures[signature] = 1
    values_sigs = list(signatures.values())
    for i in range(len(signatures.keys())):
        result = result + int((values_sigs[i]*(values_sigs[i]-1))/2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

