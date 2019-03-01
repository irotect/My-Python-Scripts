"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    palindromes = set()
    for x in range(100, 1000):
        for y in range(100, 1000):
            if is_palindrome(str(x*y)):
                palindromes.add(x*y)
    print("Largest palindrome made from product of two 3-digit number is {}".format(max(palindromes)))

