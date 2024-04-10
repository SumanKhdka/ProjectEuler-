#26: Reciprocal cycles

A = [True]*(10 ** 4)
Primes = []
for j in range(2, 10 ** 2):  # Use range() for Python 3
    if A[j] == True:
        Primes.append(j)
        for k in range(j * j, 10 ** 4, j):  # Use range() for Python 3
            A[k] = False
for j in range(10 ** 2, 10 ** 4):  # Use range() for Python 3
    if A[j] == True:
        Primes.append(j)

T = int(input())
for i in range(T):
    N = int(input())
    Primes_N = []
    Longest = 0
    Longest_Number = 0
    for Prime in Primes:
        if Prime >= N:
            break;
        else:
            Primes_N.append(Prime)
    for j in Primes_N[::-1]:
        Count = 1
        if pow(10, Count, j) == 0:
            continue
        while pow(10, Count, j) - 1 != 0:
            Count += 1
        if j - Count == 1:
            if Count >= Longest:
                Longest_Number = j
            break
        if Count >= Longest:
            Longest = Count
            Longest_Number = j
    print(Longest_Number)
