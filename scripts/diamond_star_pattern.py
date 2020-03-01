# -*- coding: utf-8 -*-
"""
Generates diamond pattern using asterisk (*):

Requirements:
    -> Python 3.0 or higher

Usage:
    -> Call the diamond_pattern(x) function where x is the size of the diamond.
"""
__script_name__ = "Diamond pattern using asterisk"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "27-02-2020"


def diamond_pattern(size):
    for i in range(1, size+1, 1):
        print(' '*(size-i) + '* '*i)

    for i in range(size-1, 0, -1):
        print(' '*(size-i) + '* '*i)


if __name__ == '__main__':
    diamond_pattern(5)
