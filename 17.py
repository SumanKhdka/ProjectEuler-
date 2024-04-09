 #17: Number to Words

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

digits = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
other = [(10**12, "Trillion"), (10**9, "Billion"), (10**6, "Million"), (1000, "Thousand"), (100, "Hundred")]

def get_word(n):
    result = ""
    for t in other:
        tmp = n // t[0]
        if (tmp > 0):
            result += get_word(tmp) + t[1]
            n -= (tmp * t[0])
    
    for t in range(len(tens)-1, -1, -1):
        tmp = n // ((t + 2) * 10)
        if (tmp > 0):
            result += tens[t]
            n -= (tmp * (t+2) * 10)
            break
    
    for t in range(len(digits)):
        if (n == (t+1)):
            result += digits[t]
            break
        
    return result

for _ in range(int(input())):
    n = int(input())
    s = get_word(n)
    l = re.split('(?<=.)(?=[A-Z])', s)
    res = ""
    for i in l:
        res += i + " "
    print(res[:-1])