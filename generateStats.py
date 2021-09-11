from solve import hillClimbing, beamSearch, variableNeigborhoodDescent, tabuSearch
from Ksat import generateKSat
import time

if __name__ == '__main__':
    k = int(input("Enter length of each clause: "))
    m = int(input("Enter the number of clauses: "))
    n = int(input("Enter the number of variables: "))

    sets = generateKSat(k, m, n, 1000)

    hc = bs3 = bs4 = vnd = ts = 0

    start = time.time()
    for set in sets:
        result = hillClimbing(set, n, m)
        if result is not None:
            hc += 1
    end = time.time()
    print("Hill Climbing took " + str(end - start) + "s to run 1000 instances")

    start = time.time()
    for set in sets:
        result = beamSearch(set, 3, n, m)
        if result is not None:
            bs3 += 1
    end = time.time()
    print("Beam Search with width 3 took " + str(end - start) + "s to run 1000 instances")

    start = time.time()
    for set in sets:
        result = beamSearch(set, 3, n, m)
        if result is not None:
            bs4 += 1
    end = time.time()
    print("Beam Search with width 4 took " +
          str(end - start) + "s to run 1000 instances")

    start = time.time()
    for set in sets:
        result = variableNeigborhoodDescent(set, n, m, 3)
        if result is not None:
            vnd += 1
    end = time.time()
    print("Variable Neighborhood Descent took " +
          str(end - start) + "s to run 1000 instances")

    start = time.time()
    for set in sets:
        result = tabuSearch(set, m, n, 2)
        if result is not None:
            ts += 1
    end = time.time()
    print("Tabu Search took " + str(end - start) + "s to run 1000 instances")

print("Stats after solving 1000 instances of k-sat")
print("Hill Climbing: ", end="")
print(hc)
print("Beam Search(width 3): ", end="")
print(bs3)
print("Beam Search:(width 4) ", end="")
print(bs4)
print("Variable Neighborhood Descent: ", end="")
print(vnd)
print("Tabu Search: ", end="")
print(ts)
