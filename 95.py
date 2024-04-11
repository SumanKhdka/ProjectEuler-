#95: Amicable chains
def main():
    limit = int(input())

    # the usual prime sieve
    primes = [2]
    for i in range(3, limit + 1, 2):
        isPrime = True

        # test against all prime numbers we have so far (in ascending order)
        for p in primes:
            # next prime is too large to be a divisor ?
            if p * p > i:
                break

            # divisible ? => not prime
            if i % p == 0:
                isPrime = False
                break

        # yes, we have a prime number
        if isPrime:
            primes.append(i)

    # initial mapping of each number to its proper divisor's sum
    divsum = [0] * (limit + 1)
    for i in range(2, limit + 1):
        sum = 1
        reduce = i
        for p in primes:
            # note: reduce itself might be prime in the end
            if p * p > reduce:
                break

            # divide by all primes
            factor = 1
            while reduce % p == 0:
                reduce //= p
                factor *= p
                factor += 1
            sum *= factor

        # if a large prime was left over
        if reduce > 1 and reduce < i:
            sum *= reduce + 1

        # subtract number itself if it isn't a prime
        if sum > 1:
            sum -= i

        divsum[i] = sum

    # loop until numbers are mapped to themselves (or get stuck in a loop)
    longestChain = 0
    smallestMember = limit
    for i in range(1, limit + 1):
        chain = [i]

        # until we:
        # 1. return to i or
        # 2. exceed the limit or
        # 3. get stuck in a loop
        while True:
            add = divsum[chain[-1]]
            chain.append(add)

            # yes, we found an amicable chain
            if add == i:
                break

            # can't be a new shorter loop:
            # we have already seen this number in an earlier iteration
            if add < i:
                break

            # abort if limit exceeded
            if add > limit:
                break

            # stuck in a loop ?
            if add in chain[:-1]:
                break

        # did we return to i ?
        if chain[-1] != i:
            continue

        # too short ?
        if len(chain) < longestChain:
            continue

        # shorter chain ?
        if longestChain < len(chain):
            longestChain = len(chain)
            smallestMember = chain[0]

    print(smallestMember)

if __name__ == "__main__":
    main()
