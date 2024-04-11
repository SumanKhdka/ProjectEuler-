 #80: Square root digital expansion
# Enter your code here. Read input from STDIN. Print output to STDOUT
import decimal
import sys

def calculate_total_digital_sum(N, P):
    total_sum = 0
    context = decimal.Context(prec=P + 5)
    decimal.setcontext(context)

    for number in range(1, N + 1):
        root = decimal.Decimal(number).sqrt()
        if root**2 != root:
            sqrt_str = str(root)[:P + 1]
            sqrt_str = sqrt_str.replace('.', '')

            if len(sqrt_str) >= P: 
                total_sum += sum(int(digit) for digit in sqrt_str[:P])

    return total_sum

N = int(sys.stdin.readline().rstrip('\n'))
P = int(sys.stdin.readline().rstrip('\n'))
result = calculate_total_digital_sum(N, P)
print(result)