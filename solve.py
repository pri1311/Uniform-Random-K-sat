from string import ascii_lowercase
from random import randint
from ksat import generateKSat


class satNode(object):
    def __init__(self, assignment, heuristic) -> None:
        super().__init__()
        self.assignment = assignment
        self.heuristic = heuristic


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

    # positive_assgn = [randint(0, 1) for i in range(0, n)]
    # negative_assgn = [abs(1 - i) for i in positive_assgn]

    positive_assgn = [1 for i in range(0, n)]
    negative_assgn = [0 for i in positive_assgn]

    assignment = dict(zip(variables, positive_assgn + negative_assgn))
    return assignment


def generateNeigbors(old_assignment, n):
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


def func(node):
    return node.heuristic


def beamSearch(set, w, n, m):

    assignment = getInitialAssignments(n)
    heuristic = calcHeuristic(set, assignment)

    open = []
    closed = []

    initialNode = satNode(assignment, heuristic)

    open.append(initialNode)
    closed.append(assignment)

    while len(open) > 0:
        open = sorted(open, key=func, reverse=True)

        currNode = open[0]
        open = open[1:]

        if currNode.heuristic == m:
            return currNode.assignment

        neigbors = generateNeigbors(currNode.assignment, n)
        for neighbor in neigbors:
            if neighbor not in closed:
                heuristic = calcHeuristic(set, neighbor)
                if len(open) == w:
                    if open[-1].heuristic <= heuristic:
                        open.pop()
                        open.append(satNode(neighbor, heuristic))
                else:
                    open.append(satNode(neighbor, heuristic))

                closed.append(neighbor)

        for node in open:
            neigbors = generateNeigbors(node.assignment, n)
            for neighbor in neigbors:
                if neighbor not in closed:
                    heuristic = calcHeuristic(set, assignment)
                    if len(open) == w:
                        if open[-1].heuristic <= heuristic:
                            open.pop()
                            open.append(satNode(neighbor, heuristic))
                    else:
                        open.append(satNode(neighbor, heuristic))
                        open = sorted(open, key=func, reverse=True)

                    closed.append(neighbor)

    return None


if __name__ == '__main__':
    k = int(input("Enter length of each clause: "))
    m = int(input("Enter the number of clauses: "))
    n = int(input("Enter the number of variables: "))

    sets = generateKSat(k, m, n, 20)
    for set in sets:
        print()
        print(set)
        assign = getInitialAssignments(n)
        print(assign)
        heuristic = calcHeuristic(set, assign)
        print(heuristic)
        result = beamSearch(set, 3, n, m)
        if result is not None:
            print("\nSolution is: ", end="")
            print(result)
            print()
        else:
            print("Solution not found")
    # set = [['b', 'c', 'C'], ['A', 'B', 'C'], ['c', 'A', 'B']]
    # print(set)
    # assign = getInitialAssignments(n)
    # print(assign)
    # heuristic = calcHeuristic(set, assign)
    # print(heuristic)
    # result = beamSearch(set, 3, n, m)
    # if result is not None:
    #     print("\nSolution is: ", end="")
    #     print(result)
    #     print()
    # else:
    #     print("Solution not found")
