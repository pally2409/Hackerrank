#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dict_cost = {}
    for i in range(len(cost)):
        if cost[i] in dict_cost.keys():
            ind = dict_cost[cost[i]]
            print(str(min(ind, i) + 1) + ' ' + str(max(ind, i) + 1))
        else:
            dict_cost[money - cost[i]] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
