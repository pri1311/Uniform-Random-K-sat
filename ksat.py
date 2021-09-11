from string import ascii_lowercase
from itertools import combinations, permutations
from random import sample


def filterClauses(k, clauses):
    resultClauses = []

    for clause in clauses:
        hashMap = []
        valid = True
        for i in range(0, k):
            if clause[i].lower() in hashMap:
                valid = False
                break
            hashMap.append(clause[i].lower())

        if valid:
            resultClauses.append(clause)

    return resultClauses


def generateKSat(k, m, n, limit=None):
    if limit is None:
        limit = 10

    if n < k:
        raise ValueError("Invalid Constraints")
    positive_var = (list(ascii_lowercase))[:n]
    negative_var = [c.upper() for c in positive_var]
    variables = positive_var + negative_var

    clauses = list(combinations(variables, k))

    clauses = filterClauses(k, clauses)

    tempSets = []

    i = 0

    while i < limit:
        c = sample(clauses, m)
        if c not in tempSets:
            i += 1
            tempSets.append(list(c))

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

    print(len(sets))
    for set in sets:
        print(set)
