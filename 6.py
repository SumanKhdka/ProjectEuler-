#6: Sum square difference

#!/bin/python3

import sys


t = int(input())
for _ in range(t):
    n = int(input())
    square_of_sum = (n * (n + 1) // 2) ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    print(square_of_sum - sum_of_squares)