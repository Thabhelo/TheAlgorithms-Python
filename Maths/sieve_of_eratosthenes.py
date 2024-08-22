'''There is a classic algorithm in number theory that I thought can be a great addition to this Maths subdirectory: The 'Sieve of Eratosthenes'. 
It's an efficient way to find all prime numbers up to a given limit.
'''

def sieve_of_eratosthenes(n):
  """
  Finds all prime numbers up to a given number n using the Sieve of Eratosthenes.

  This algorithm efficiently determines all primes less than or equal to n by iteratively marking multiples of primes as non-prime.

  Args:
    n: The upper limit for finding prime numbers (inclusive).

  Returns:
    A list containing all the prime numbers less than or equal to n.
  """

  # Create a list of booleans, where primes[i] is True if i is prime, False otherwise.
  primes = [True] * (n + 1)

  # 0 and 1 are not prime by definition
  primes[0] = primes[1] = False

  # Efficiently iterate only up to the square root of n
  # Numbers greater than the square root of n cannot have prime factors
  # greater than the square root
  for p in range(2, int(n**0.5) + 1):
    if primes[p]:  # If p is prime
      # Mark all multiples of p as non-prime (composite)
      for i in range(p * p, n + 1, p):
        primes[i] = False

  # Return a list of all remaining primes (where primes[i] is True)
  return [i for i in range(2, n + 1) if primes[i]]

# This is how you would use it, say:
n = 100
prime_numbers = sieve_of_eratosthenes(n)
print(prime_numbers)

'''Complexity Analysis:

For the Time Complexity:

Best Case: O(n) (when n is small)
Average Case: O(n log log n)
Worst Case: O(n log log n) 👍 ✅ 

For Space Complexity: O(n)
'''
