from string import ascii_lowercase
from itertools import combinations
from random import shuffle


def generateKSat(k, m, n):
    if 2 * n < k:
        raise ValueError("Invalid Constraints")
    positive_var = (list(ascii_lowercase))[:n]
    negative_var = [c.upper() for c in positive_var]
    variables = positive_var + negative_var

    clauses = list(combinations(variables, k))
    sets = list(combinations(clauses, m))

    shuffle(sets)
    sets = sets[:5]

    for set in sets:
        print(set)


if __name__ == '__main__':
    k = int(input("Enter length of each clause: "))
    m = int(input("Enter the number of clauses: "))
    n = int(input("Enter the number of variables: "))

    generateKSat(k, m, n)
