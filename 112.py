def find_least_number(proportion):
    count_bouncy = 0
    number = 99
    while True:
        number += 1
        str_num = str(number)
        increasing = decreasing = True
        for i in range(1, len(str_num)):
            if str_num[i] > str_num[i - 1]:
                decreasing = False
            elif str_num[i] < str_num[i - 1]:
                increasing = False
            if not increasing and not decreasing:
                count_bouncy += 1
                break
        if count_bouncy / number >= proportion:
            return number

# Input
test_cases = int(input())
results = []

for _ in range(test_cases):
    x, y = map(int, input().split())
    result = find_least_number(y / 100)
    results.append(result)

# Output
for result in results:
    print(result)
