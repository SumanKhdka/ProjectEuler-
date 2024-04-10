#28: Number spiral diagonals

T = int(input())
for i in range(T):
    N = (int(input()) - 1) // 2
    print((16 * N ** 3 + 30 * N ** 2 + 26 * N + 3) // 3 % (10 ** 9 + 7))
