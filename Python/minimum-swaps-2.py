#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    minVal = min(arr)
    minSwaps = 0
    i = 0
    while(i<len(arr)-1):
        print(i)
        if arr[i]!=minVal+i:
            temp = arr[(arr[i]+minVal)-2]
            arr[(arr[i]+minVal)-2] = arr[i]
            arr[i] = temp
            minSwaps = minSwaps+1
        if arr[i]== minVal+i:
            i = i + 1     
    return minSwaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

