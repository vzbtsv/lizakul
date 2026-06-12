from math import *


f = open("26_3377.txt").readlines()

n = int(f[0])

data = sorted([list(map(int, x.split())) for x in f[1:]])

d = {}

for x in data:
    row, seat = x

    if row in d.keys():
        d[row].append(seat)

    else:
        d[row] = [seat]


def p1(r):
    k = 0
    if len(r) == 2 and r[1] - r[0] <= 2:
        return 0

    for i in range(len(r) - 1):
        x1 = r[i]
        x2 = r[i + 1]

        if x2 - x1 > 2:
            k += 1
            if x2 - x1 <= 4:
                k -= 1

    return k + 1


res = []
for x in d:
    row = d[x]
    res.append((x, p1(d[x])))

print(sum([x[1] for x in res]))
print(sorted(res, key=lambda x: x[1]))
