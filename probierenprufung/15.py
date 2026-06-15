
def f(x, a1, a2):
    L = 114567 <= x <= 221379
    N = 189516 <= x <= 374110
    D = a1 <= x <= a2

    res = (L <= D) and ((not N) or D)
    return res




print(374110 - 114567)

Ox = []

for x in [114567, 221379, 189516, 374110]:
    Ox.append(x - 1)
    Ox.append(x)
    Ox.append(x + 1)


Ox = sorted(Ox)
t = []

for a1 in Ox:
    for a2 in Ox:
        if a1 < a2:
            if all([f(x, a1, a2) for x in Ox]):
                t.append(a2 - a1)

print(min(t))


