#!/bin/python3

import math
import os
import random
import re
import sys
os.environ["OUTPUT_PATH"] = "junk.txt"
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    %timeit l1 = [0 for _ in range(n)]
    for q in range(len(queries)):
        i,j,k = queries[q]
        for n in range(i-1,j):
            l1[n] = l1[n]+k 
    #l1 = [sum(k for q in range(len(queries)) for i, j, k in queries[q] if i - 1 <= n < j) for n in range(n)]

    print(l1)    
    return max(l1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
