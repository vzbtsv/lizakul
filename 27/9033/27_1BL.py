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
s3 = []
s1k = []
s2k = []
f = open('/Users/elizavetakulesova/Downloads/27-123b.txt')
for line in f:
    x, y, type = line.split()
    x, y = float(x), float(y)
    if y > 22 and int(type[1]) >= 8:
        s1.append([x, y, type])
    elif x > 22 and int(type[1]) >= 8:
        s2.append([x, y, type])
    elif int(type[1]) >= 8:
        s3.append([x, y, type])



suma = 0
cnt = 0
for el in s1:
    for elem in s1:
        if el == elem:
            continue
        suma += leen(el, elem)
        cnt += 1
for el in s2:
    for elem in s2:
        if el == elem:
            continue
        suma += leen(el, elem)
        cnt += 1
for el in s3:
    for elem in s3:
        if el == elem:
            continue
        suma += leen(el, elem)
        cnt += 1
print(suma * 10000 / cnt)
mini = 10 ** 16
for el in s1:
    for elem in s2:
        mini = min(mini, leen(el, elem))
    for elem in s3:
        mini = min(mini, leen(el, elem))
for el in s2:
    for elem in s3:
        mini = min(mini, leen(el, elem))
print(mini * 10000)
'''
1495 16955
54154 12041 
'''
