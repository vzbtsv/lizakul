import re
from math import hypot

f= open("27A.txt").readlines()

def find_cluster(x, y):
    if y > 10:
        return 0
    return 1


clusters = [[], []]
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

c1 = center(clusters[0])
c2 = center(clusters[1])

orange_subgiants_pat = r"N.IV"

orange_subgiants_1 = list(filter(lambda x: re.fullmatch(orange_subgiants_pat, x[1]), clusters[0]))
orange_subgiants_2 = list(filter(lambda x: re.fullmatch(orange_subgiants_pat, x[1]), clusters[1]))
# print(orange_subgiants_1)
# print(orange_subgiants_2)

res = []

for os in orange_subgiants_1:
    res.append(r(c2, os))

for os in orange_subgiants_2:
    res.append(r(c1, os))


A1 = int(abs(min(res) * 10000))
A2 = int(abs(max(res) * 10000))

print(A1, A2)