#94: Almost equilateral triangles

import math

# valid perimeters
solutions = []

# return true if area is integral
def isValidTriangle(oneSide, twoSides):
    check = 4 * twoSides * twoSides - oneSide * oneSide
    root = math.sqrt(check)
    return root * root == check

# brute-force approach
def findMore(perimeter, limit):
    # check all perimeters
    while perimeter <= limit + 3:
        # length of the two equal sides
        twoSides = perimeter // 3

        # assume single side is one unit smaller than the other two sides
        oneSide = twoSides - 1
        if isValidTriangle(oneSide, twoSides):
            solutions.append(perimeter - 1)

        # assume single side is one unit bigger than the other two sides
        oneSide = twoSides + 1
        if isValidTriangle(oneSide, twoSides):
            solutions.append(perimeter + 1)

        # next group of triangles
        perimeter += 3

    return perimeter

# just compute sequence
def sequence(limit):
    # initial values of the equal sides
    plusOne = [1, 5]
    minusOne = [1, 17]

    solutions.clear()
    # smallest solutions where:
    solutions.append(3 * plusOne[1] + 1) # single side is 1 unit longer than the equal sides
    solutions.append(3 * minusOne[1] - 1) # single side is 1 unit shorter than the equal sides

    while solutions[-1] <= limit + 3:
        # compute next length of equal sides
        nextPlusOne = 14 * plusOne[1] - plusOne[0] - 4
        nextMinusOne = 14 * minusOne[1] - minusOne[0] + 4

        # store it, shift off oldest values
        plusOne[0] = plusOne[1]
        plusOne[1] = nextPlusOne
        minusOne[0] = minusOne[1]
        minusOne[1] = nextMinusOne

        # we are interested in the perimeter
        solutions.append(3 * nextPlusOne + 1)
        solutions.append(3 * nextMinusOne - 1)

    # largest perimeter found
    return solutions[-1]

def main():
    solutions.append(16) # perimeter of smallest triangle
    perimeter = 18 # check 18-1 and 18+1 in next step

    tests = int(input())
    while tests:
        limit = 1000000000
        limit = int(input())

        # check all perimeters
        while perimeter <= limit + 3:
            perimeter = sequence(limit)

        # sum of all relevant triangles
        sum = 0
        for x in solutions:
            if x <= limit:
                sum += x

        print(sum)
        tests -= 1

if __name__ == "__main__":
    main()
