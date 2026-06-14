import re
from math import hypot

f = open("27B.txt").readlines()
clusters = [[], [], []]

def find_cluster(x, y):
    if x < 20:
        if y > 23:
            return 0
        return 1
    return 2




for star in f:
    x, y, add = star.replace(",", ".").split()
    x = float(x)
    y = float(y)

    clusters[find_cluster(x, y)].append([(x, y), add])


clusters = sorted(clusters, key=len)


def r(d1, d2):
    return hypot(d1[0][0] - d2[0][0], d1[0][1] - d2[0][1])

# for x in clusters:
#     print(len(x))


def center(cluster):
    res = []

    for c1 in cluster:
        res.append((sum([r(c1, c2) for c2 in cluster]), c1))

    return min(res)[1]

res = []
for cluster1 in clusters:
    for cluster2 in clusters:
        if cluster1 != cluster2:
            bright_pat = r".[89]"
            bright_stars_1 = list(filter(lambda x: re.match(bright_pat, x[1]), cluster1))
            bright_stars_2 = list(filter(lambda x: re.match(bright_pat, x[1]), cluster2))
            for b1 in bright_stars_1:
                for b2 in bright_stars_2:
                    res.append(r(b1, b2))


B1 = min(sorted(res))
print(res)

res = []
for cluster in clusters:
    bright_pat = r".[89]"
    bright_stars = list(filter(lambda x: re.match(bright_pat, x[1]), cluster))

    for b1 in bright_stars:
        for b2 in bright_stars:
            if r(b1, b2):
                res.append(r(b1, b2))

B2 = sum(res) / len(res)
print(B2)


print(int(abs(B1 * 10000)), int(abs(B2 * 10000)))