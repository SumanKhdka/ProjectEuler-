// #21: Amicable numbers
#include <iostream>
#include <set>

// generate sum of all divisor's of x (where x > 1)
unsigned int getSum(unsigned int x)
{
  // find all factors:
  // look only for the "smaller" divisors <= sqrt(x)
  // and they have a "bigger" brother x / divisor

  // 1 is always a divisor, but not the number x itself
  unsigned int divisorSum = 1;
  // therefore start at 2
  for (unsigned int divisor = 2; divisor * divisor <= x; divisor++)
    if (x % divisor == 0)
    {
      divisorSum += divisor;

      // add the "bigger brother"
      auto otherDivisor = x / divisor;
      // except square numbers
      if (otherDivisor != divisor)
        divisorSum += otherDivisor;
    }

  return divisorSum;
}

int main()
{
  // contain all numbers which are part of an amicable pair
  std::set<unsigned int> amicables;

  // precomputation step:
  // find all amicable numbers <= 100000
  const unsigned int MaxAmicable = 100000;
  for (unsigned int i = 2; i <= MaxAmicable; i++)
  {
    auto sibling = getSum(i);

    // found a pair ?
    if (i == getSum(sibling) && i != sibling)
    {
      amicables.insert(i);
      amicables.insert(sibling);
    }
  }

  // and now start processing input
  unsigned int tests;
  std::cin >> tests;
  while (tests--)
  {
    unsigned int x;
    std::cin >> x;

    // just look up all suitables numbers
    unsigned int sum = 0;
    for (auto i : amicables)
    {
      // discard those that are too big
      if (i > x)
        break;
      // note: an set::set is sorted ascendingly by default

      // yes, accept that amicable number
      sum += i;
    }

    std::cout << sum << std::endl;
  }
  return 0;
}