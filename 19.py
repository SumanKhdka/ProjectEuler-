# Enter your code here. Read input from STDIN. Print output to STDOUT
m_days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(y):
    if y % 100 == 0:
        return (True if y % 400 == 0 else False)
    if y % 4 == 0:
        return(True)
    else:
        return(False)
    
def no_of_leapyear(y):
    if y[0] > 2000:
        return (100//4 + (y[0]-2000)//4 - (y[0]-2000)//100 + (y[0]-2000)//400 - (1 if is_leap(y[0]) and (y[1] == 1 or (y[1] == 2 and y[2] <= 28)) else 0))
    else:
        return ((y[0]-1900)//4 - (1 if is_leap(y[0]) and (y[1] == 1 or (y[1] == 2 and y[2] <= 28)) else 0))
    

for a0 in range(int(input())):
    
    y1, y2 = list(map(int, input().split())), list(map(int, input().split()))
    
    if not y1[2] == 1:
        if y1[1] == 12:
            y1 = [y1[0]+1, 1, 1]
        else:
            y1 = [y1[0], y1[1]+1, 1]
    
    diffy1 = 365 * (y1[0] - 1900) + sum(m_days[:y1[1]]) + (y1[2] - 1) + no_of_leapyear(y1)
    
    sundays = 1 if diffy1 % 7 == 6 else 0
    
    diffy1 = 6 - diffy1 % 7
    
    if y1[0] == y2[0]:
        if y1[1] > y2[1]:
            print(0)
            continue
        elif y1[1] == y2[1]:
            print(sundays)
            continue
    elif y1[0] > y2[0]:
        print(sundays)
        continue
     
    while not y1[0] > y2[0] and not (y1[0] == y2[0] and y1[1] >= y2[1]):
        
        d =(m_days[y1[1]] + 1) if y1[1] == 2 and is_leap(y1[0]) else m_days[y1[1]]
            
        if d % 7 == diffy1:
            sundays = sundays + 1
        
        diffy1 = (diffy1 - d % 7) if d % 7 <= diffy1 else (7-(d % 7)+diffy1)
        
        if y1[1] == 12:
            y1 = [y1[0]+1, 1, 1]
        else:
            y1 = [y1[0], y1[1]+1, 1]
            
    print(sundays)
     