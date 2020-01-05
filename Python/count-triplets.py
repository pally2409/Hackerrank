#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplet_count = 0 
    right_map = {}
    left_map = {}
    for i in range(len(arr)):
        if arr[i] in right_map.keys():
            right_map[arr[i]] = right_map[arr[i]] + 1
        else:
            right_map[arr[i]] = 1
    for i in range(len(arr)):
        right_map[arr[i]] = right_map[arr[i]] - 1
        if arr[i]/r in left_map.keys() and arr[i] * r in right_map.keys():
            triplet_count = triplet_count + left_map[arr[i]/r] * right_map[arr[i]*r]
        if arr[i] in left_map.keys():
            left_map[arr[i]] = left_map[arr[i]] + 1
        else: 
            left_map[arr[i]] = 1
    return triplet_count   




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

