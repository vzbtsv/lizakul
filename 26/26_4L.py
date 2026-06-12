f = open('/Users/elizavetakulesova/Downloads/26_20828.txt')
k, m, n = map(int, f.readline().split())
g = int(f.readline())
s = []
for line in f:
    s.append(list(map(int, line.split())))
mtx = [[[0 for j in range(n)] for _ in range(m)] for i in range(k)]
s.sort(key=lambda x: (x[0], x[1]))
# print(s)
cnt = 0
dct = dict()
for el in s:
    flag = False
    for i in range(k):
        for j in range(m):
            for ii in range(n):
                if mtx[i][j][ii] <= el[0]:
                    mtx[i][j][ii] = el[1] + 1
                    cnt += 1
                    if i == 0:
                        if j in dct:
                            dct[j] += 1
                        else:
                            dct[j] = 1
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
print(cnt)
ans = 10 ** 10
idx = 0
for el in dct:
    if dct[el] < ans:
        ans = dct[el]
        idx = el + 1
print(idx)
