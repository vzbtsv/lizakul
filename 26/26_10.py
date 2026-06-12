f = open("26_9711.txt").readlines()

m, n = list(map(int, f[0].split()))

samokats = [[0, []] for i in range(m)]

data = sorted([list(map(int, x.split())) for x in f[1:]])
maxx = (-9999, 0)
allmax = -9999
res2 = []
for x in data:
    start_time = x[0]
    end_time = start_time + x[1]
    start_place = x[2]
    end_place = x[3]

    samokats[start_place - 1][0] += 1
    samokats[start_place - 1][1].append(end_time)

    for i in range(len(samokats)):
        for j in range(len(samokats[i][1])):
            if samokats[i][1][j] < start_time:
                samokats[i][1][j] = 999999999
                samokats[i][0] -= 1

    col_of_samokats = sum([x[0] for x in samokats])
    res2.append((col_of_samokats, start_time))

    for i in range(len(samokats)):
        maxx = max((samokats[i][0], i + 1), maxx)

for x in samokats:
    print(x[0])

print(maxx)
print(max(res2))