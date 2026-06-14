from fnmatch import *



def divs(n):
    res = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)


    res = sorted(list(res))
    if res:
        simples = list(filter(lambda x: simple(x), res))

    if len(res) == 32:
        return simples

    return False



def simple(d):
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            return False

    return True



for i in range(10 ** 6, 0, -1):
    if fnmatch(str(i), "5*"):
        r = divs(i)
        if r:
            print(i, len(r))
