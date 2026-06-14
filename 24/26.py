f = open('/Users/elizavetakulesova/Downloads/26_30046.txt')
n = int(f.readline())
s = []
uch = [0] * 10000
for line in f:
    beg, cont, real = map(int, line.split())
    if real == 1:
        s.append([beg, cont])
s.sort(key=lambda x: (x[1], x[0]))
cnt = 0
for el in s:
    if sum(uch[el[0] - 1: el[0] + el[1]]) == 0:
        cnt += 1
        for i in range(el[0] - 1, el[0] + el[1]):
            uch[i] = 1
print(uch[::-1].index(1))
print(cnt)
