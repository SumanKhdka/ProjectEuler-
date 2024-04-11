#74: Digit factorial chains

# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import sys
import math
import time



def fac(n):
    res = 0
    for num in str(n):
        res += FACTORIAL10[int(num)]
    return res

FACTORIAL10 = [math.factorial(i) for i in range(10)]

mem = {}
def get_chain(n):
    chain = []
    while True:
        chain.append(n)
        if n in mem:
            n = mem[n]
        else:
            i = fac(n)
            mem[n] = i
            n = i
        if n in chain:
            break
    return chain

# circular chains up to 10^6
circular_chains = {
    #[145, 145]
    145: 1,
    #[169, 363601, 1454, 169]
    169: 3,
    #[871, 45361, 871]
    871: 2,
    #[872, 45362, 872]
    872: 2,
    #[1454, 169, 363601, 1454]
    1454: 3,
    #[40585, 40585]
    40585: 1,
    #[45361, 871, 45361]
    45361: 2,
    #[45362, 872, 45362]
    45362: 2,
    #[363601, 1454, 169, 363601]
    363601: 3,
}

inputs = [tuple(map(int, input().strip().split())) for _ in range(int(input().strip()))]

st = time.time()

seen = {}
for N, L in inputs:
    res = []
    for i in range(N + 1):
        chain = 0
        if i in circular_chains:
            chain = circular_chains[i]
        else:
            s = "".join(sorted(str(i)))
            chain = seen[s] if s in seen else len(get_chain(i))
            seen[s] = chain
        if chain == L:
            res.append(i)
    if len(res) > 0:
        print(" ".join(map(str, res)))
    else:
        print(-1)
