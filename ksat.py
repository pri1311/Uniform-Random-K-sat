from string import ascii_lowercase
from itertools import combinations, permutations
from random import shuffle, sample


def generateKSat(k, m, n, limit=None):
    if limit is None:
        limit = 10

    if 2 * n < k:
        raise ValueError("Invalid Constraints")
    positive_var = (list(ascii_lowercase))[:n]
    negative_var = [c.upper() for c in positive_var]
    variables = positive_var + negative_var

    clauses = list(combinations(variables, k))
    # tempSets = list(permutations(clauses, m))

    tempSets = []

    i = 0

    while i < limit:
        c = sample(clauses, m)
        if c not in tempSets:
            i += 1
            tempSets.append(list(c))

    shuffle(tempSets)
    tempSets = tempSets[:limit]

    sets = []

    for tempSet in tempSets:
        temp = []
        for clause in tempSet:
            temp.append(list(clause))
        sets.append(temp)
    return sets


if __name__ == '__main__':
    k = int(input("Enter length of each clause: "))
    m = int(input("Enter the number of clauses: "))
    n = int(input("Enter the number of variables: "))

    sets = generateKSat(k, m, n)
    for set in sets:
        print(set)
