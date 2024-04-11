#72: Counting fractions
# Enter your code here. Read input from STDIN. Print output to STDOUT

lookup=[i for i in range(10**6+1)]
for i in range(2,10**6+1):
    if lookup[i]==i:
        for j in range(i,10**6,i):
            lookup[j]-=lookup[j]//i
for i in range(3,10**6):
    lookup[i]+=lookup[i-1]
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(lookup[n])