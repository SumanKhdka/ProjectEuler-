#97: Large non-Mersenne prime

Digits = 10
Modulo = 10000000000
#else
Digits = 12
Modulo = 1000000000000
#endif

# compute the n-th power of a big number (n >= 0)
def powmod(base, exponent, modulo):
    result = 1
    while exponent > 0:
        # fast exponentiation
        if exponent & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        exponent >>= 1
    return result

def main():
    sum = 0

    tests = int(input())
    for _ in range(tests):
        # read a * b^c + d
        factor, base, exponent, add = map(int, input().split())

        # compute result
        result = (powmod(base, exponent, Modulo) * factor + add) % Modulo

        # modulo all the way ... we need only the last 10 (or 12) digits
        sum += result
        sum %= Modulo

    # print with leading zeros
    print(f"{sum:0{Digits}d}")

if __name__ == "__main__":
    main()
