# 23: Non-abundant sums

def Sum_Of_Divisors(Number, Primes):
    Sum = 1
    Factor = Number
    i = 0
    while i < len(Primes) and Primes[i] ** 2 <= Factor and Factor > 1:
        if Factor % Primes[i] == 0:
            Temp = Primes[i] ** 2
            Factor = Factor / Primes[i]
            while Factor % Primes[i] == 0:
                Temp *= Primes[i]
                Factor = Factor / Primes[i]
            Sum *= (Temp - 1) / (Primes[i] - 1)
        i += 1
    if Factor > 1:
        Sum *= Factor + 1
    return Sum - Number


A = []
Primes = []
for j in range(0, int(10 ** 2.5)):  # Use range here
    A.append(True)
for j in range(2, int(10 ** 1.25)):  # Use range here
    if A[j] == True:
        Primes.append(j)
        for k in range(j * j, int(10 ** 2.5), j):  # Use range here
            A[k] = False
for j in range(int(10 ** 1.25), int(10 ** 2.5)):  # Use range here
    if A[j] == True:
        Primes.append(j)

Abundant = []
for i in range(12, 28124):  # Use range here
    if Sum_Of_Divisors(i, Primes) > i:
        Abundant.append(i)

T = int(input())
for i in range(T):
    N = int(input())
    Flag = False
    if N > 28123:
        print("YES")
    else:
        for i in range(len(Abundant)):
            for j in range(i, len(Abundant)):
                if Abundant[i] + Abundant[j] == N:
                    print("YES")
                    Flag = True
                    break
                elif Abundant[i] + Abundant[j] > N:
                    break
            if Flag == True:
                break
        if Flag == False:
            print("NO")
