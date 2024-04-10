 #22: Names scores

N = int(input())
Names = []
for i in range(N):
    Names.append(input())
Names.sort()
Q = int(input())
for i in range(Q):
    Result = 0
    Name = input()
    for j in range(len(Name)):
        Result += ord(Name[j]) - 64
    print((Names.index(Name) + 1) * Result)
