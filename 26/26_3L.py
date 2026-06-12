f = open('/Users/elizavetakulesova/Downloads/26_17643-2.txt')
n = int(f.readline())
s = []
s2 = dict()
dct = dict()
for line in f:
    art, cost, stat = map(int, line.split())
    if cost > 558:
        s.append([art, cost, stat])
    if stat == 0:
        if art in dct:
            dct[art] += 1
        else:
            dct[art] = 1
    else:
        if art in s2:
            s2[art] += 1
        else:
            s2[art] = 1

maxi = 0
for el in dct:
    if maxi < dct[el]:
        maxi = dct[el]
    # if dct[el] == 51:
    #     print(el)
# print(maxi)
m_cost = 0
anss = [51786, 46481, 37134]
ans2 = set()
for el in s:
    if el[0] in anss:
        m_cost = max(el[1], m_cost)
        if m_cost == 856:
            ans2.add(el[0])
for el in s2:
    if el in ans2:
        print(s2[el], el)
print(51 * 856)
