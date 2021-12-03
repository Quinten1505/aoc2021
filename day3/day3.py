def filterRating(arr):
    newArr = []
    arrT = list(map(list, zip(*arr)))
    dom = 1
    if arrT[0].count(0) < len(arr)/2:
        dom = 0
    for entry in arr:
        if entry[0] == dom:
            newArr.append(entry)

    return newArr

with open('day3.txt') as day3:
    lines = day3.readlines()

    data = [[] for i in range(len(lines))]
    for i, line in zip(range(len(lines)),lines):
        data[i][:0] = list(map(int, line.strip()))

    newData = list(map(list, zip(*data)))
    gamma = [1 if entry.count(1) > len(lines)/2 else 0 for entry in newData]
    epsilon = [0 if x == 1 else 1 for x in gamma]

    newGamma = int("".join(list(map(str, gamma))),2)
    newEpsilon = int("".join(list(map(str, epsilon))),2)
    
    print('The answer to the first puzzle of day 3:', newGamma*newEpsilon)

    test = filterRating(data)
    print(test)