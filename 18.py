#18: Maximum path sum I

# Enter your code here. Read input from STDIN. Print output to STDOUT
maxsum = [0]

def max_sum(t, l, i, lsum):
    m, n = i, i+1
    if l == len(t) - 1:
        maxsum[0] = max(maxsum[0], lsum + t[l][m], lsum + t[l][n])
        return
    max_sum(t, l + 1, m, lsum + t[l][m])
    max_sum(t, l + 1, n, lsum + t[l][n])

for _ in range(int(input())):
    triangle, lvl, maxsum[0] = [], int(input()), 0
    for i in range(lvl):
        triangle.append(list(map(int, input().split())))
        
    if lvl > 1:
        max_sum(triangle, 1, 0, triangle[0][0])
    print(max(maxsum[0], triangle[0][0]))