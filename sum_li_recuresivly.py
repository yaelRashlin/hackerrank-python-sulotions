'''
https://www.hackerrank.com/challenges/simple-array-sum/problem?h_r=next-challenge&h_v=zen
'''

#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    if len(ar) == 1:
        return ar[0]
    return ar[0] + simpleArraySum(ar[1:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input().strip())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
