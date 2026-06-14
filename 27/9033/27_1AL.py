def leen(a, b):
    x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(s):
    ans = 10 ** 10
    t = [0, 0, 0]
    for el in s:
        suma = 0
        for elem in s:
            suma += leen(el , elem)
        if suma < ans:
            ans = suma
            t = el
    return t


s1 = []
s2 = []
s1k = []
s2k = []
f = open('/Users/elizavetakulesova/Downloads/27-123a.txt')
for line in f:
    x, y, type = line.split()
    x, y = float(x), float(y)
    if y > 8:
        s1.append([x, y, type])
        if type[2:] == 'VII':
            s1k.append([x, y, type])
    else:
        s2.append([x, y, type])
        if type[2:] == 'VII':
            s2k.append([x, y, type])


cen1 = center(s1)
cen2 = center(s2)
mini1 = 10 ** 10
maxi = -1
for el in s1k:
    mini1 = min(mini1, leen(el, cen1))
    maxi = max(maxi, leen(el, cen1))
for el in s2k:
    mini1 = min(mini1, leen(el, cen2))
    maxi = max(maxi, leen(el, cen2))
print(mini1 * 10000, maxi * 10000)

'''
1495 16955
'''
