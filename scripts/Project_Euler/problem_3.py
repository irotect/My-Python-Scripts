# Largest Prime Factor



def prime_factors(n):
    factors = [1,n]
    term = n
    for x in range(2, int(n**0.5)+1):
        #print("taking in {}".format(x))
        while term % x == 0:
            factors.append(x)
            term = term/x
    factors.sort()
    return factors


if __name__ == "__main__":
    N = 600851475143
    print("Largest prime factor of {} is {}".format(N, prime_factors(N)[-1]))
