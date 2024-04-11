 #71: Ordered fractions

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


t = int(input())

for i in range(t):
    a, b, n = [int(x) for x in input().split()]
    inv_a = modinv(a, b)
    r = n % b
    d = r - inv_a
    if d < 0:
        d += b
    den = n - d
    num = (den * a - 1) // b
    print("{} {}".format(num, den))