import math

# greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    size = int(input())

    # triangles where right angle is in the origin
    result = size * size

    # plus triangles where the right angle is located on the x-axis
    result += size * size
    # plus triangles where the right angle is located on the y-axis
    result += size * size

    # now all triangles where the right angle at point P(x > 0, y <= x)
    # that's the triangle in the bottom-right half, denoted by slashes
    # ^   /
    # | //
    # | ///
    # |////
    # +--->

    for p_x in range(1, size + 1):
        for p_y in range(1, p_x + 1):
            # reduce to a proper fraction
            factor = gcd(p_x, p_y)
            deltaX = p_x // factor
            deltaY = p_y // factor

            found = 0

            # assume Q is "below" P
            q_x = p_x - deltaY
            q_y = p_y + deltaX
            while q_x >= 0 and q_y <= size:
                found += 1
                q_x -= deltaY
                q_y += deltaX

            # assume Q is "above" P
            q_x = p_x + deltaY
            q_y = p_y - deltaX
            while q_y >= 0 and q_x <= size:
                found += 1
                q_x += deltaY
                q_y -= deltaX

            # mirror along y=x when p_y < p_x
            if p_x != p_y:
                found *= 2

            result += found

    print(result)

if __name__ == "__main__":
    main()
