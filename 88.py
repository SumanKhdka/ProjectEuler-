#88: Product-sum numbers

def valid(n, k):
    if k >= len(minK):
        return False
    if minK[k] > n:
        minK[k] = n
        return True
    return False

def getMinK(n, product, sum, depth=1, minFactor=2):
    if product == 1:
        return valid(n, depth + sum - 1)

    result = 0
    if depth > 1:
        if product == sum:
            return valid(n, depth)
        if valid(n, depth + sum - product):
            result += 1

    for i in range(minFactor, int(product**0.5) + 1):
        if product % i == 0:
            result += getMinK(n, product // i, sum - i, depth + 1, i)

    return result

def main():
    limit = int(input())
    global minK
    minK = [9999999] * (limit + 1)

    n = 4
    sum = 0
    todo = limit - 1
    while todo > 0:
        found = getMinK(n, n, n)
        if found > 0:
            todo -= found
            sum += n
        n += 1

    print(sum)

if __name__ == "__main__":
    main()
