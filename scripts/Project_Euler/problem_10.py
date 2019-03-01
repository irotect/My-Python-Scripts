"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from scripts.Project_Euler.problem_3 import prime_factors


def list_primes_less_then(n):
    primes = []
    x = 2
    while x < n:
        print(f"taking in {x}")
        if len(prime_factors(x)) == 2:
            primes.append(x)
        x+=1
    return primes


if __name__ == "__main__":
    a=list_primes_less_then(2000000)
    print(a)
    print(sum(a))

