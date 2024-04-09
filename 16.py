 #16: Power digit sum
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    sn = str(2**n)
    ans = 0
    for d in sn:
        ans += int(d)
    print(ans)