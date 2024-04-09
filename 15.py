# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
for i in range(int(input())):
    n, m=map(int, input().split())
    print(math.comb(n+m, m) %(10**9+7))