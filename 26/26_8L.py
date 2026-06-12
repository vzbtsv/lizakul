f = open('/Users/elizavetakulesova/Downloads/26_25363.txt')
n = int(f.readline())
s = []
spc = [0] * n
i = 0
for line in f:
    i += 1
    wait, act = map(int, line.split())
    if wait <= act:
        s.append([i, wait, 1])
    else:
        s.append([i, act, 2])
s.sort(key=lambda x: x[1])
l = 0
r = n - 1
ans = 0
idx = 0
print(s)
for el in s:
    if el[2] == 1:
        spc[l] = el[0]
        ans = el[0]
        idx = l
        l += 1
    else:
        spc[r] = el[0]
        ans = el[0]
        idx = r
        r -= 1
print(ans)
idx += 1
print(n - idx)
