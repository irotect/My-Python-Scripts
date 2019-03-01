"""
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

natural_numbers = range(1,101)


def sum_of_squares(lst):
    return sum(map(lambda a: a**2, lst))


def square_of_sum(lst):
    return sum(lst)**2


if __name__ == "__main__":
    print("square of sums = {}\nsum of squares = {}\ndifference of square of sum and sum of square = {}".format(square_of_sum(natural_numbers),sum_of_squares(natural_numbers),square_of_sum(natural_numbers)-sum_of_squares(natural_numbers)))
