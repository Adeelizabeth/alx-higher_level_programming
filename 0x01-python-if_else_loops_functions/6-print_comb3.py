#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combination of two digit in ascending order.

    The two digits must be different - 01 and 10 are considered Identical.
    """
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
