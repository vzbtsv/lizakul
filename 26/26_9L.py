f = open('/Users/elizavetakulesova/Downloads/26_3377.txt')
n = int(f.readline())
dct = dict()
for line in f:
    rd, place = map(int, line.split())
    if rd in dct:
        dct[rd].append(place)
    else:
        dct[rd] = [place]

ans = 0
maxi = -1
cnt = 0
for el in dct:
    dct[el] = sorted(dct[el])
    s = dct[el]
    frd = 0
    flag = False
    for i in range(len(s) - 1):
        if flag:
            flag = False
            continue
        if s[i + 1] - s[i] > 2:
            frd += 1
            if s[i + 1] - s[i] <= 4:
                flag = True
    if not flag:
        frd += 1
    if frd > maxi:
        maxi = max(maxi, frd)
        cnt = el
    ans += frd
print(ans, cnt)
