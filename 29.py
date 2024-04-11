 #29: Distinct powers

# I called it "limit" in the explanation
maxExponent = int(input())

# 2^17 > 10^5 (max. input)
MaxBasePower = 16

# if a^b = base^(exponent*basePower)
# then b = (1..n) but exponent*basePower = (basePower, 2*basePower, 3*basePower, ..., n*basePower)
# store for each product exponent*basePower the smallest basePower
minExponent = [0] * ((maxExponent+1)*MaxBasePower)
for i in range(1, MaxBasePower + 1):
    for j in range(1, maxExponent + 1):
        if minExponent[i*j] == 0:
            minExponent[i*j] = i

# all "a" which can be composed as base^exponent, stored as [a] => [base]
base = [0] * (maxExponent + 1)

# how often numbers were used multiple times (those are the collisions we are looking for)
repeated = 0

# analyze all bases
for x in range(2, maxExponent + 1): # maximum base is maxExponent, too
    parent = base[x]
    if parent == 0: # no
        power = x * x
        while power <= maxExponent:
            base[power] = x
            power *= x
        continue

    exponent = 0
    reduce = x
    while reduce > 1:
        reduce //= parent
        exponent += 1

    for y in range(2, maxExponent + 1):
        if minExponent[y * exponent] < exponent:
            repeated += 1

# there are (maxExponent-1)^2 combinations, subtract all duplicates
all = maxExponent - 1
result = all * all - repeated
print(result)
