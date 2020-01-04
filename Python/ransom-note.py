#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    len_mag = len(magazine)
    len_note = len(note)
    dict_mag = {}
    dict_note = {}

    for i in range(max(len_mag,len_note)):
        if(i < len_mag):
            if magazine[i] in dict_mag.keys():
                dict_mag[magazine[i]] = dict_mag[magazine[i]] + 1
            else: 
                dict_mag[magazine[i]] = 1
        if(i < len_note):
            if note[i] in dict_note.keys():
                dict_note[note[i]] = dict_note[note[i]] + 1
            else: 
                dict_note[note[i]] = 1
    note_k = list(dict_note.keys())
    ctr = 0
    for i in range(len(note_k)):
        if note_k[i] in dict_mag.keys():
            if dict_note[note_k[i]] <= dict_mag[note_k[i]]:
                ctr = ctr + 1
            else:      
                break 
        else:
            break 
    if(ctr == len(note_k)):
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
