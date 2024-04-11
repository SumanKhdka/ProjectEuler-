#75: Singular integer right triangles

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math,itertools,bisect

lookup=[0]*(5*10**6+1)
for v,u in itertools.combinations(range(1,int((5*10**6)**0.5)+1,2),2):
        if u>v and math.gcd(u,v)==1:
            s=u**2+u*v
            for i in range(s,5*10**6+1,s):
                lookup[i]+=1
ans=[i for i in range(5*10**6+1) if lookup[i]==1]
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    count=bisect.bisect_right(ans,n)
    print(count)