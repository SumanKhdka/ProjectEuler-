#25: N-digit Fibonacci number

from math import log10
from math import ceil

T = int(input())
for i in range(T):
    N = int(input())
    """
    i = 0
    Count = 2
    Numbers = [1,1,1]
    while Numbers[i] <= 10 ** (N - 1):
        i = (i + 1) % 3
        Count += 1
        Numbers[i] = Numbers[(i + 1) % 3] + Numbers[(i + 2) % 3]
    print Count
    """
    print(int(ceil((N - 1 + log10(5) / 2) / log10((1 + 5 ** 0.5) / 2))))

