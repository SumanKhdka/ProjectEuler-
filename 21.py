#21: Amicable numbers

def sum_of_divisors(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum = sum + i + n//i
            else:
                sum = sum + i
            i += 1
    return sum

def find_amicable_numbers(N):
    amicable_sum = 0
    for a in range(1, N):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum


T = int(input())
for _ in range(T):
    N = int(input())
    print(find_amicable_numbers(N))
