import re
from math import hypot

f= open("27B.txt").readlines()

def find_cluster(x, y):
    if x <= 20:
        if y >= 23:
            return 0
        return 1
    return 2


clusters = [[], [], []]
for star in f:
    x, y, add = star.replace(",", ".").split()

    x = float(x)
    y = float(y)

    clusters[find_cluster(x, y)].append([(x, y), add])

clusters = sorted(clusters, key=len)

def r(d1, d2):
    return hypot(d1[0][0] - d2[0][0], d1[0][1] - d2[0][1])

def center(cluster):
    res = []

    for c1 in cluster:
        res.append([sum([r(c1, c2) for c2 in cluster]), c1])

    return min(res)[1]


green_carlic_pat = r"J.V"

cluster_b1 = list(filter(lambda x: re.fullmatch(green_carlic_pat, x[1]), clusters[-1]))
cluster_b2 = list(filter(lambda x: re.fullmatch(green_carlic_pat, x[1]), clusters[0]))

B1 = max(cluster_b1, key=lambda x: x[0][0])[0][0]
B2 = max(cluster_b2, key=lambda x: x[0][1])[0][1]

B1 = int(abs(B1 * 10000))
B2 = int(abs(B2 * 10000))


print(B1, B2)