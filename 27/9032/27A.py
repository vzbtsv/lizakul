import re
from math import hypot

f = open("27A.txt").readlines()


def find_cluster(x, y):
    if y > 10:
        return 0
    return 1


all_stars = []
clusters = [[], []]
for star in f:
    x, y, add = star.replace(",", ".").split()
    x = float(x)
    y = float(y)

    clusters[find_cluster(x, y)].append([(x, y), add])
    all_stars.append([(x, y), add])

clusters = sorted(clusters, key=len)

for x in clusters:
    print(len(x))


def r(d1, d2):
    return hypot(d2[0][0] - d1[0][0], d2[0][1] - d1[0][1])


def center(cluster):
    summ = []

    for c1 in cluster:
        summ.append((sum([r(c1, c2) for c2 in cluster]), c1))

    return min(summ)[1]


blue3_pat = r"L3"

blue3 = list(filter(lambda x: re.match(blue3_pat, x[1]), all_stars))

cmin = center(clusters[0])
cmax = center(clusters[-1])

A1 = []
A2 = []
for b in blue3:
    A1.append(r(b, cmin))
    A2.append(r(b, cmax))


print(int(abs(max(A1) * 10000)), int(abs(max(A2) * 10000)))