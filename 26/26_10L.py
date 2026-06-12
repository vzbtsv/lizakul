f = open('/Users/elizavetakulesova/Downloads/26_9711.txt')
m, n = map(int, f.readline().split())
s = [0] * (60 * 24)
dct = dict()
for i in range(1, m + 1):
    dct[i] = [0] * (60 * 24)
for line in f:
    st, cont, nb, nf = map(int, line.split())
    if st + cont + 1 > 60 * 24:
        for j in range(st, 60 * 24):
            s[j] += 1
    else:
        for j in range(st, st + cont + 1):
            s[j] += 1
    for j in range(st, 60 * 24):
        dct[nb][j] -= 1
    for j in range(st + cont + 1, 60 * 24):
        dct[nf][j] += 1
ans = 0
cnt = 0
for el in dct:
    if min(dct[el]) < 0:
        kk = abs(min(dct[el]))
        if kk > ans:
            ans = kk
            cnt = el
print(cnt, s.index(max(s)))