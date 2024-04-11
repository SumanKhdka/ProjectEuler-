# Enter your code here. Read input from STDIN. Print output to STDOUT

def euler_totient(limit):
    phi = [i for i in range(limit + 1)]
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi

def find_min_ratio(limit):
    phi = euler_totient(limit)
    min_ratio = float('inf')
    min_n = 0
    for n in range(2, limit + 1):
        if sorted(str(n)) == sorted(str(phi[n])):  # Check if n and phi(n) are permutations
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n
    return min_n

# Sample input
limit = int(input())
result = find_min_ratio(limit)
print(result)