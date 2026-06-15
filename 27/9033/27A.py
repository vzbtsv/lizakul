import re
from math import hypot

f = open("27A.txt").readlines()
clusters = [[], []]

def find_cluster(x, y):
    if y > 10:
        return 0
    return 1



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
        res.append((sum([r(c1, c2) for c2 in cluster]), c1))

    return min(res)[1]


res = []
for cluster in clusters:
    c = center(cluster)
    quasar_pat = r"..VII"
    quasars = list(filter(lambda x: re.fullmatch(quasar_pat, x[1]), cluster))

    for q in quasars:
        if r(q, c):
            res.append(r(q, c))



print(int(abs(min(res) * 10000)), int(abs(max(res) * 10000)))