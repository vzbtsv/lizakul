f = open('/Users/elizavetakulesova/Downloads/26_2717.txt')
n = int(f.readline())
s = dict()
for line in f:
    rd, st = map(int, line.split())
    if rd not in s:
        s[rd] = [st]
    else:
        s[rd].append(st)
ans = 10 ** 10
cnt = 0
for el in s:
    s[el].sort()
    s[el] = s[el][::-1]
    if len(s[el]) < 5:
        continue
    spc = s[el]
    cont = 1
    num = 0
    r = spc[0]
    for i in range(len(spc) - 1):
        if spc[i] - 3 <= spc[i + 1]:
            cont += 1
        else:
            r = spc[i + 1]
            cont = 1
        if cont == 5:
            num = r
            break
    if el < ans and num != 0:
        ans = el
        cnt = num

print(ans, cnt)