# Enter your code here. Read input from STDIN. Print output to STDOUT

ans = {}
prime_list = [2, 3, 5, 7, 11, 13, 17]


def divisors(num: int) -> int:
    global prime_list
    if num == 1:
        return 1
    n_factors = 1
    for p in prime_list:
        count = 1
        while num % p == 0:
            count += 1
            num //= p
        n_factors *= count
        if pow(p, 2) >= num:
            break
    if num > 1:
        n_factors *= 2
        if num not in prime_list:
            prime_list.append(num)
    return n_factors


def triangle_num_factors(n: int) -> int:
    return divisors(n // 2) * divisors(n + 1) if n % 2 == 0 else divisors(n) * divisors((n + 1) // 2)


def sum_of_series(x):
    return x * (x + 1) // 2

i = 1
for n in range(1, 1001):
    while triangle_num_factors(i) <= n:
        i += 1
    ans[n] = i

for _ in range(int(input())):
    print(sum_of_series(ans[int(input())]))