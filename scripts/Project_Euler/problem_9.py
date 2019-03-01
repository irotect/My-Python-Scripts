"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


def pythagoras_check(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False


if __name__ == "__main__":
    for x in range(1,1000):
        for y in range(1,1000):
            z = 1000-x-y
            if x+y+z == 1000:
                print("taking {}".format((x,y,z)))
                if pythagoras_check(x,y,z):
                    print("{}^2 + {}^2 = {}^2\n\n {} + {} + {} = {}".format(x,y,z,x,y,z,x+y+z))
                    print("product : {}".format(x*y*z))
                    exit(0)
