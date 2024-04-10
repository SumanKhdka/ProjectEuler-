#27: Quadratic primes

A = [True] * (10 ** 5)  
Primes = []
for j in range(2, int(10 ** 2.5)): 
    if A[j] == True:
        Primes.append(j)
        for k in range(j * j, int(10 ** 5), j): 
            A[k] = False
for j in range(int(10 ** 2.5), int(10 ** 5)): 
    if A[j] == True:
        Primes.append(j)

N = int(input())  
n = a_max = b_max = n_max = 0
i = 0
Primes_b = []
while Primes[i] <= N:
    Primes_b.append(Primes[i])
    i += 1

for b in Primes_b:
    for a in range(-b, b, 2):  
        n = 0
        while A[n * n + a * n + b]:
            n += 1
        if n > n_max:
            n_max = n
            a_max = a
            b_max = b

print(a_max, b_max)  
