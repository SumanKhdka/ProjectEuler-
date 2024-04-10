#24: Lexicographic permutations

import math

def factorial(n):
  """
  This function calculates the factorial of a non-negative integer n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

T = int(input())
for i in range(T):
  Result = ""
  Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
  Count = 0
  N = int(input())
  N -= 1
  for j in range(0, 13):
    if N // factorial(13 - j - 1) == 0 or j == 12:
      Result += Letters[0]
      Letters.pop(0)
      Count += 1
    else:
      index = N // factorial(13 - j - 1)  # Use integer division
      Result += Letters[index]
      Letters.pop(index)
      N = N % factorial(13 - j - 1)
      Count += 1
  print(Result)
