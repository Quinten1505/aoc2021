with open('day2.txt') as day2:
    lines = day2.readlines()

    data = {"forward": [0] * len(lines), "down": [0] * len(lines), "up": [0] * len(lines), "depth": [0] * len(lines), "newDepth": [0] * len(lines), "horizontal": [0] * len(lines)}
    for i, line in zip(range(len(lines)), lines):
        x, y = line.strip().split()
        data[x][i] = int(y)
        data['depth'][i] = data['depth'][i-1] + data['down'][i] - data['up'][i]
        data['horizontal'][i] = data['horizontal'][i-1] + data['forward'][i]
        data['newDepth'][i] = data['newDepth'][i-1] + data['depth'][i]*data['forward'][i]

    print('The answer to puzzle 1 day 2:',data['depth'][-1]*data['horizontal'][-1])
    print('The answer to puzzle 2 day 2:',data['newDepth'][-1]*data['horizontal'][-1])