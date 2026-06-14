from fnmatch import *
def f(n):
    dct = dict()
    i = 2
    while n > 1:
        if n % i == 0:
            n //= i
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        else:
            i += 1
    ans = 1
    for el in dct:
        ans *= (dct[el] + 1)
    return [ans, len(dct)]

# print(f(14))
for i in range(1, 10 ** 6):
    if fnmatch(str(i), '23*4?5'):
        k = f(i)
        if k[0] == 32:
            print(i, k[1])
