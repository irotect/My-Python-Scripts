"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def multiply_list(lst):
    result = 1
    for x in map(int, lst):
        result = result * x
    return result


if __name__ == "__main__":
    divisors = range(1,21)

    for x in range(1, multiply_list(divisors)):
        for y in divisors:
            if not x%y == 0:
                break
        else:
            print("{} is smallest number divisible by 1 to 20".format(x))
            break
