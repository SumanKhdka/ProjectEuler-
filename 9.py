#!/bin/python3

import sys


t = int(input())
for _ in range(t):
    n = int(input())
    largest = -1
    for a in range(1, n // 3 + 1):
        b = n* (a - n // 2) // (a - n)
        c = n - a - b
        if a * a + b * b == c * c and (product := a * b * c) > largest:
            largest = product
    print(largest)
