#77: Prime summations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_partitions(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in primes:
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
    if is_prime(n):  # If n itself is prime, count it as one way
        dp[n] += 1
    return dp[n]

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(prime_partitions(n))
