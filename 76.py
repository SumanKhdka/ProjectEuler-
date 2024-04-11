#76: Counting summations

# Enter your code here. Read input from STDIN. Print output to STDOUT

def getways(n):
    res=[0]*(n+1)
    res[0]=1
    for i in range(1,n):
        for j in range(i,n+1):
            res[j]+=res[j-i]%(10**9+7)
    return res[n]%(10**9+7)

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(getways(n))