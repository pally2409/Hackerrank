#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from queue import PriorityQueue
# Complete the largestRectangle function below.

# Problem explanation:
# As each building can be the beginning of a rectangle of a particular height, we keep appending to the stack, thereby, continuing the building of the min height in the stack. However, with each value appended, there is an active building of that particular value as well. Now suppose, we come across a value whose value is lesser than the previous value in the stack. The building of the height corresponding to the top of the stack is now over. So, we pop that element. Find its height from the height array, multiply it by finding the width from the current value of the iterator i, subtracted by the value of the next value (new top of the stack) because that height is lesser than the height of the height we just popped and hence, cannot be a part of the building of that height. 
def largestRectangle(h):
    stack_h = []
    i = 0
    max_area = 0
    while(i < len(h)):
        if len(stack_h) == 0 or h[i] >= h[stack_h[-1]]:
            stack_h.append(i)
            i += 1
        else:
            val = stack_h.pop()
            temp_area = h[val] * ((i - stack_h[-1] - 1) if len(stack_h) > 0 else i)
            if temp_area > max_area:
                max_area = temp_area
    while len(stack_h) != 0:
        val = stack_h.pop()
        temp_area = h[val] * ((i - stack_h[-1] - 1) if len(stack_h) > 0 else i)
        if temp_area > max_area:
            max_area = temp_area
    return max_area



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

