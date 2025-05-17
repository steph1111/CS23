"""
File:       calc.py
Author:     Stephanie L'Heureux
Email:      stephanielh1111@gmail.com
Due:        Tue Mar 4, 2025 7:00pm
CS23:       Program One (Sets)
"""

import sys
import math


def r_derangement(n):
    """
    Number of permutations for a set of `n` elements in which no elements
    appear in their original position.
    """
    if n == 0:
        return 1
    if n == 1:
        return 0
    else:
        return (n - 1) * (r_derangement(n - 1) + r_derangement(n - 2))


if __name__ == "__main__":
    derangements = {
        0:  1,
        1:  0,
        2:  1,
        3:  2,
        4:  9,
        5:  44,
        6:  265,
        7:  1854,
        8:  14833,
        9:  133496,
        10: 1334961,
        11: 14684570,
        12: 176214841,
        13: 2290792932
    }

    for line in sys.stdin:
        calc = line.split()
        try:
            if "choose" in calc:
                n, k = int(calc[0]), int(calc[2])
                print(math.comb(n, k))
            elif "permute" in calc:
                n, k = int(calc[0]), int(calc[2])
                print(math.perm(n, k))
            elif "rderangement" in calc:
                n = int(calc[1])
                print(r_derangement(n))
            elif "derangement" in calc:
                n = int(calc[1])
                print(derangements[n])
            else:
                print("Please enter valid input")
        except (ValueError, IndexError):
            print("Please enter valid input")
        except KeyError:
            print("Choose a smaller value")
