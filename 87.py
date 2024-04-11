//#87: Prime power triples
def main():
    MaxLimit = 100 * 1000 * 1000 # Hackerrank: 10^7 instead of 5*10^6

    # prime sieve
    primes = [2]
    for i in range(3, int(MaxLimit**0.5) + 1, 2):
        isPrime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    # generate all sums
    sums = []
    for a in primes:
        for b in primes:
            for c in primes:
                a2 = a * a
                b3 = b * b * b
                c4 = c * c * c * c
                sum = a2 + b3 + c4
                if sum > MaxLimit:
                    break
                sums.append(sum)

    # sort ascendingly and remove duplicates
    sums.sort()
    sums = list(dict.fromkeys(sums)) # Remove duplicates using a dictionary

    # process test cases
    tests = int(input())
    for _ in range(tests):
        limit = MaxLimit
        limit = int(input())

        # find next sum which is bigger than the limit
        pos = next((i for i, x in enumerate(sums) if x > limit), len(sums))
        # how many sums are in between 28 and limit ?
        num = pos
        print(num)

if __name__ == "__main__":
    main()
