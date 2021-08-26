import time

from Ksat import generateKSat
from helper import (
    getInitialAssignments,
    calcHeuristic,
    generateNeighbors,
    generateNeighbors2,
    generateNeighbors3,
    generateTabuNeighbors,
    getBestNeigbor,
    func
)


class satNode(object):
    def __init__(self, assignment, heuristic) -> None:
        super().__init__()
        self.assignment = assignment
        self.heuristic = heuristic


def hillClimbing(set, n, m):
    assignment = getInitialAssignments(n)
    heuristic = calcHeuristic(set, assignment)

    maxHeuristic = heuristic

    currNode = satNode(assignment, heuristic)

    while True:
        if currNode.heuristic == m:
            return currNode.assignment

        node = None

        neighbors = generateNeighbors(currNode.assignment, n)

        for neighbor in neighbors:
            heuristic = calcHeuristic(set, neighbor)

            if heuristic >= maxHeuristic:
                node = neighbor
                maxHeuristic = heuristic

        if node is None:
            return None

        currNode = satNode(node, maxHeuristic)


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

        # print(currNode.assignment, currNode.heuristic)

        neighbors = generateNeighbors(currNode.assignment, n)
        for neighbor in neighbors:
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
            neighbors = generateNeighbors(node.assignment, n)
            for neighbor in neighbors:
                if neighbor not in closed:
                    heuristic = calcHeuristic(set, neighbor)
                    if len(open) == w:
                        if open[-1].heuristic <= heuristic:
                            open.pop()
                            open.append(satNode(neighbor, heuristic))
                    else:
                        open.append(satNode(neighbor, heuristic))
                        open = sorted(open, key=func, reverse=True)

                    closed.append(neighbor)

    return None


def variableNeigborhoodDescent(set, n, m, kMax):
    assignment = getInitialAssignments(n)
    heuristic = calcHeuristic(set, assignment)

    closed = []

    maxHeuristic = heuristic
    currNode = satNode(assignment, heuristic)
    closed.append(assignment)

    k = 1

    while k <= kMax:
        print(k)
        if currNode.heuristic == m:
            return currNode.assignment

        node = None

        if k == 1:
            neighbors = generateNeighbors(currNode.assignment, n)
        elif k == 2:
            neighbors = generateNeighbors2(currNode.assignment, n)
        elif k == 3:
            neighbors = generateNeighbors3(currNode.assignment, n)

        for neighbor in neighbors:
            if neighbor not in closed:
                heuristic = calcHeuristic(set, neighbor)

                if heuristic >= maxHeuristic:
                    node = neighbor
                    maxHeuristic = heuristic

        if node is None:
            k += 1
        else:
            currNode = satNode(node, maxHeuristic)
            closed.append(node)
            k = 1

    return None


def tabuSearch(set, m, n, tenure):
    assignment = getInitialAssignments(n)
    heuristic = calcHeuristic(set, assignment)
    memory = [0 for i in range(0, n)]

    tabuList = []

    currNode = satNode(assignment, heuristic)
    tabuList.append(assignment)

    while True:
        if currNode.heuristic == m:
            return currNode.assignment

        for i in range(0, n):
            if memory[i] > 0:
                memory[i] -= 1

        neighbors = generateTabuNeighbors(
            currNode.assignment, n, memory)

        if len(neighbors) == 0:
            return None

        while True:
            node, heuristic, i, j = getBestNeigbor(set, neighbors)
            neighbors.remove((node, i, j))

            if node not in tabuList:
                currNode = satNode(node, heuristic)
                tabuList.append(node)
                memory[i] = memory[j] = tenure
                break

            elif len(neighbors) == 0:
                return None


if __name__ == '__main__':
    k = int(input("Enter length of each clause: "))
    m = int(input("Enter the number of clauses: "))
    n = int(input("Enter the number of variables: "))

    sets = generateKSat(k, m, n, 3)
    for set in sets:
        # time.sleep(1)
        print()
        print(set)
        assign = getInitialAssignments(n)
        print(assign)
        heuristic = calcHeuristic(set, assign)
        print(heuristic)
        # result = variableNeigborhoodDescent(set, n, m, 3)
        result = tabuSearch(set, m, n, 2)
        if result is not None:
            print("\nSolution is: ", end="")
            print(result)
            print()
        else:
            print("Solution not found")
        # result = beamSearch(set, 3, n, m)
        # if result is not None:
        #     print("\nSolution is: ", end="")
        #     print(result)
        #     print()
        # else:
        #     print("Solution not found")
    # Gives different solutions for beam search and Hill Climbing
    # set = [['D', 'G', 'J'], ['C', 'H', 'I'], ['c', 'h', 'I'], ['c', 'i', 'J']]
    # set = [['b', 'B', 'C'], ['D', 'E', 'I'], [
    #     'a', 'd', 'B'], ['C', 'D', 'F']]  # 3 4 10
    # print(set)
    # assign = getInitialAssignments(n)
    # print(assign)
    # heuristic = calcHeuristic(set, assign)
    # print(heuristic)
    # result = hillClimbing(set, n, m)
    # if result is not None:
    #     print("\nSolution is: ", end="")
    #     print(result)
    #     print()
    # else:
    #     print("Solution not found")
    # result = beamSearch(set, 3, n, m)
    # if result is not None:
    #     print("\nSolution is: ", end="")
    #     print(result)
    #     print()
    # else:
    #     print("Solution not found")
    # result = variableNeigborhoodDescent(set, n, m, 3)
    # if result is not None:
    #     print("\nSolution is: ", end="")
    #     print(result)
    #     print()
    # else:
    #     print("Solution not found")
    print(len(sets))

# 2 6 5