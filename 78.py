#78: Coin partitions

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import cycle
import sys
sys.setrecursionlimit(10**6) 

t = int(input())
p = []
p.append(1) # p(0) = 1
penta = [1]

for num in range(t):
    a = int(input())
    n = len(p)
    
    while(n <= a):
        i = 0
        p.append(0)
        
        signs = [1, 1, -1, -1]
        sign = cycle(signs)

        while(penta[i] <= n):

            p[n] += next(sign) * p[n - penta[i]] # Generative sequence p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + ..
            p[n] %= (10**9 + 7)
            i += 1

            if(len(penta) <= i):
                if(i % 2 == 0): # Pentagonal numbers use m of m = 0, +/- 1, +/- 2, +/- 3, ....
                    m = (i // 2) + 1
                else:
                    m = -1 * (i // 2 + 1)    

                k = m * (3 * m - 1) // 2 #Pentagonal numbers 0.5m*(3m - 1)
                penta.append(k)
            

        n += 1
    
    print(p[a])