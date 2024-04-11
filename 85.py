//#85: Counting rectangles
import math

def main():
    tests = int(input())
    for _ in range(tests):
        target = int(input())

        # assume x <= y, therefore x <= sqrt(limit)
        root = math.sqrt(target)
        best_rectangles = 0
        best_area = 0
        for x in range(1, int(root) + 2): # allow slight overshooting
            # start with a square
            y = x
            # number of rectangles
            rectangles = 0

            # slowly increase y until too many rectangles in the grid
            while True:
                area = x * y

                # the formula derived above
                rectangles = x * (x + 1) * y * (y + 1) // 4

                # closer to desired number of rectangles than before ?
                if abs(best_rectangles - target) > abs(rectangles - target):
                    best_rectangles = rectangles
                    best_area = area

                # prefer larger areas, too (additional requirement of Hackerrank)
                if abs(best_rectangles - target) == abs(rectangles - target) and best_area < area:
                    best_area = area

                y += 1
                if rectangles >= target:
                    break

            # just a speed-up ... abortion when the inner loop exited with a square area x*y
            # => it means that no further solutions possible, area already too large
            if y == x + 1: # plus one because y was incremented before leaving the inner loop
                break

        print(best_area)

if __name__ == "__main__":
    main()
