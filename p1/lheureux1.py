"""
File:       lheureux1.py
Author:     Stephanie L'Heureux
Email:      stephanielh1111@gmail.com
Due:        Tue Mar 4, 2025 7:00pm
CS23:       Program One (Sets)
"""
from random import sample, randint
from itertools import combinations


def print_set(name: str, S: set):
    """
    Formatted print for sets.
    """
    print(f"{name} = {S if S else '{}'}")


def P(S):
    """
    Power set of `S`.
    """
    return (set(s) for i in range(len(S) + 1) for s in combinations(S, i))

 
def print_p_set(name, S):
    """
    Formatted print for power set.
    """
    print(f"{name} = {{{', '.join(str(ele) if ele else '{}' for ele in S)}}}")
    

def main():
    # Fill A with with (randomly) 3 to 5 random integers in the range 1 ... 10.
    A = set(sample(range(1, 11), randint(3, 5)))
    # Fill B with with (randomly) 1 to 3 random integers in the range 1 ... 10.
    B = set(sample(range(1, 11), randint(1, 3)))

    # Print out A and B
    print_set("A", A)
    print_set("B", B)

    # A - B and B - A
    print_set("A - B", A - B)
    print_set("B - A", B - A)

    # Subsets
    print("A ⊂ B", A <= B)
    print("B ⊂ A", B <= A)

    # Powersets
    print_p_set("P(A)", P(A))
    print_p_set("P(B)", P(B))


if __name__ == "__main__":
    main()
