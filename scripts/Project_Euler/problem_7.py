"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
from scripts.Project_Euler.problem_3 import prime_factors


def list_nth_prime(n):
    primes = []
    x = 2
    while len(primes) < n:
        if len(prime_factors(x)) == 2:
            #print(x)
            primes.append(x)
        x += 1
    return primes


if __name__ == "__main__":
    print(list_primes(10001)[-1])
