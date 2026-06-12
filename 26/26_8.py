f = open("26_25363.txt").readlines()

n = int(f[0])

data = [list(map(int, x.split())) for x in f[1:]]
data2 = []

for i in range(len(data)):
    x = data[i]
    data2.append((x[0], 0, i + 1))
    data2.append((x[1], 1, i + 1))

last_set = [0 for i in range(len(data2))]
data2 = sorted(data2)

for x in data2:
    t, state, ind = x
    if ind not in last_set:
        if not state:
            for i in range(len(last_set)):
                if last_set[i] == 0:
                    last_set[i] = ind
                    print(ind)
                    print(i)
                    break

        else:
            for i in range(len(last_set) - 1, 0, -1):
                if last_set[i] == 0:
                    last_set[i] = ind
                    print(ind)
                    print(i)
                    break

print(len(last_set) - 1475)
print(len(data2))
print(len(last_set))
# for x in data:
#     print(x)
