#34: Digit factorials

#!/bin/python3

import os
from math import factorial
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def dF(n):
    # Write your code here
    total = 0

    for i in range(10, n):
        digit_sum = sum(factorial(int(digit)) for digit in str(i))
        if digit_sum % i == 0:
            total += i

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    
    fptr.write(str(dF(n)))

    fptr.close()
