import re
from math import hypot

f = open("27B.txt").readlines()


def find_cluster(x, y):
    if x < 20:
        if y > 23:
            return 0
        return 1
    return 2


all_stars = []
clusters = [[], [], []]
for star in f:
    x, y, add = star.replace(",", ".").split()
    x = float(x)
    y = float(y)

    clusters[find_cluster(x, y)].append([(x, y), add])
    all_stars.append([(x, y), add])

blue3_pat = r"L"
clusters = sorted(clusters, key=lambda x: len(list(filter(lambda y: re.match(blue3_pat, y[1]), x))))

for x in clusters:
    print(len(x), len(list(filter(lambda y: re.match(blue3_pat, y[1]), x))))


def r(d1, d2):
    return hypot(d2[0][0] - d1[0][0], d2[0][1] - d1[0][1])


def center(cluster):
    summ = []

    for c1 in cluster:
        summ.append((sum([r(c1, c2) for c2 in cluster]), c1))

    return min(summ)[1]


cmin = center(clusters[0])
cmax = center(clusters[-1])

B1 = r(cmin, cmax)

res = []
for cluster1 in clusters:
    for cluster2 in clusters:
        blue_1 = list(filter(lambda x: re.match(blue3_pat, x[1]), cluster1))
        blue_2 = list(filter(lambda x: re.match(blue3_pat, x[1]), cluster2))

        for b1 in blue_1:
            for b2 in blue_2:
                res.append(r(b1, b2))

B2 = max(res)



print(int(abs(B1 * 10000)), int(abs(B2 * 10000)))