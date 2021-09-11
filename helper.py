from string import ascii_lowercase
from random import randint


def calcHeuristic(set, assignment):
    heuristic = 0
    for clause in set:
        for i in clause:
            if assignment[i] == 1:
                heuristic += 1
                break
    return heuristic


def getInitialAssignments(n):
    positive_var = (list(ascii_lowercase))[:n]
    negative_var = [c.upper() for c in positive_var]
    variables = positive_var + negative_var

    positive_assgn = [randint(0, 1) for i in range(0, n)]

    negative_assgn = [abs(1 - i) for i in positive_assgn]

    # positive_assgn = [1 for i in range(0, n)]
    # negative_assgn = [0 for i in positive_assgn]

    assignment = dict(zip(variables, positive_assgn + negative_assgn))
    return assignment


def generateNeighbors(old_assignment, n):
    positive_var = (list(ascii_lowercase))[:n]

    neighbors = []

    for i in range(0, n):
        new_assignment = old_assignment.copy()
        new_assignment[positive_var[i]] = abs(
            1 - new_assignment[positive_var[i]])
        new_assignment[positive_var[i].upper()] = abs(
            1 - new_assignment[positive_var[i].upper()])

        neighbors.append(new_assignment)

    return neighbors


def generateNeighbors2(old_assignment, n):
    positive_var = (list(ascii_lowercase))[:n]

    neighbors = []

    for i in range(0, n):
        for j in range(i + 1, n):
            new_assignment = old_assignment.copy()
            new_assignment[positive_var[i]] = abs(
                1 - new_assignment[positive_var[i]])
            new_assignment[positive_var[i].upper()] = abs(
                1 - new_assignment[positive_var[i].upper()])
            new_assignment[positive_var[j]] = abs(
                1 - new_assignment[positive_var[i]])
            new_assignment[positive_var[j].upper()] = abs(
                1 - new_assignment[positive_var[i].upper()])

            neighbors.append(new_assignment)

    return neighbors


def generateNeighbors3(old_assignment, n):
    positive_var = (list(ascii_lowercase))[:n]

    neighbors = []

    for i in range(0, n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                new_assignment = old_assignment.copy()
                new_assignment[positive_var[i]] = abs(
                    1 - new_assignment[positive_var[i]])
                new_assignment[positive_var[i].upper()] = abs(
                    1 - new_assignment[positive_var[i].upper()])
                new_assignment[positive_var[j]] = abs(
                    1 - new_assignment[positive_var[i]])
                new_assignment[positive_var[j].upper()] = abs(
                    1 - new_assignment[positive_var[i].upper()])
                new_assignment[positive_var[l]] = abs(
                    1 - new_assignment[positive_var[i]])
                new_assignment[positive_var[l].upper()] = abs(
                    1 - new_assignment[positive_var[i].upper()])

                neighbors.append(new_assignment)

    return neighbors


def generateTabuNeighbors(old_assignment, n, memory):
    positive_var = (list(ascii_lowercase))[:n]

    neighbors = []

    for i in range(0, n):

        if memory[i] != 0:
            continue

        for j in range(i + 1, n):

            if memory[j] != 0:
                continue

            new_assignment = old_assignment.copy()
            new_assignment[positive_var[i]] = abs(
                1 - new_assignment[positive_var[i]])
            new_assignment[positive_var[i].upper()] = abs(
                1 - new_assignment[positive_var[i].upper()])
            new_assignment[positive_var[j]] = abs(
                1 - new_assignment[positive_var[i]])
            new_assignment[positive_var[j].upper()] = abs(
                1 - new_assignment[positive_var[i].upper()])

            neighbors.append((new_assignment, i, j))

    return neighbors


def getBestNeigbor(set, neighbors):
    maxHeuristic = -1
    node = None
    i = j = -1

    for neighbor in neighbors:
        heuristic = calcHeuristic(set, neighbor[0])

        if heuristic > maxHeuristic:
            maxHeuristic = heuristic
            node = neighbor[0]
            i = neighbor[1]
            j = neighbor[2]

    return node, maxHeuristic, i, j


def testCasesOrRandom():
    print('1. Run Test Cases')
    print('2. Solve Uniform Random K - Sat')
    choice = int(input())

    if choice == 2:
        return False
    return True


def printAlgorithmOptions():
    print('1. Hill Climbing')
    print('2. Beam Search')
    print('3. Variable Neighborhood Descent')
    print('4. Tabu Search')


def printResult(result):
    if result is not None:
        print("\nSolution is: ", end="")
        print(result)
        print()
    else:
        print("\nSolution not found\n")


def printInitial(set, n):
    # print(set)
    prettyPrint(set)
    print("Initial Assignment is: ", end="")
    assignment = getInitialAssignments(n)
    print(assignment)
    print("Initial Heuristic Value is: ", end="")
    print(calcHeuristic(set, assignment))


def readTestCase(choice):
    testcase = []

    with open('./testcases/testcase' + str(choice) + '.txt', 'r') as f:
        testcase = f.readlines()

    k = int(testcase[0])
    m = int(testcase[1])
    n = int(testcase[2])
    set = []

    for i in range(3, len(testcase)):
        set.append(testcase[i].split(' ')[:-1])

    return k, m, n, set


def func(node):
    return node.heuristic


def prettyPrint(set):
    n = len(set)
    m = len(set[0])
    for i in range(0, n):
        print("(", end="")
        for j in range(0, m):
            if (j < m - 1):
                print(set[i][j], end=" ∨ ")
            else:
                print(set[i][j], end=")")
        if i < n - 1:
            print(" ∧ ", end="")
    print()
