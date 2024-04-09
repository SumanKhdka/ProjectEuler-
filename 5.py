#5: Smallest multiple

#!/bin/python3

import sys


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

t = int(input())
for _ in range(t):
    product = 1
    n = int(input())
    for number in range(2, n + 1):
        product *= number // gcd(product, number)
    print(product)