#13: Large sum

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = 0
for _ in range(n):
    x = int(input())
    s += x
ss = str(s)
print(ss[:10])