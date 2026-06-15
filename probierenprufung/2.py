from itertools import product, permutations


def f(x, y, z ,w):
    res = ((not y) and (w <= z) and (not y)) and ((w == x) or ((y and z) == x))

    return res



for a in product([0, 1], repeat=6):
    table = {(a[0], 1, a[1], 1),
             (a[2], 1, a[3], a[4]),
             (1, 1, a[5], 1)}


    for p in permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))


