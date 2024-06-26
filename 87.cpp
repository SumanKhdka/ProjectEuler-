//#87: Prime power triples
#include <vector>
#include <algorithm>
#include <iostream>

int main()
{
  const unsigned int MaxLimit = 100 * 1000 * 1000; // Hackerrank: 10^7 instead of 5*10^6

  // prime sieve
  std::vector<unsigned int> primes;
  primes.push_back(2);
  for (unsigned int i = 3; i*i < MaxLimit; i += 2)
  {
    bool isPrime = true;

    // test against all prime numbers we have so far (in ascending order)
    for (auto p : primes)
    {
      // next prime is too large to be a divisor ?
      if (p*p > i)
        break;

      // divisible ? => not prime
      if (i % p == 0)
      {
        isPrime = false;
        break;
      }
    }

    // yes, we have a prime number
    if (isPrime)
      primes.push_back(i);
  }

  // just three nested loops where I generate all sums
  std::vector<unsigned int> sums;
  for (auto a : primes)
    for (auto b : primes)
      for (auto c : primes)
      {
        auto a2 = a*a;
        auto b3 = (unsigned long long)b*b*b;
        auto c4 = (unsigned long long)c*c*c*c;
        auto sum = a2 + b3 + c4;
        // abort if too big
        if (sum > MaxLimit)
          break;

        sums.push_back(sum);
      }

  // sort ascendingly
  std::sort(sums.begin(), sums.end());
  // a few sums occur twice, let's remove them !
  auto last = std::unique(sums.begin(), sums.end());

  // process test cases
  unsigned int tests = 1;
  std::cin >> tests;
  while (tests--)
  {
    unsigned int limit = MaxLimit;
    std::cin >> limit;

    // find next sum which is bigger than the limit
    auto pos = std::upper_bound(sums.begin(), last, limit);
    // how many sums are inbetween 28 and limit ?
    auto num = std::distance(sums.begin(), pos);
    std::cout << num << std::endl;
  }

  return 0;
}