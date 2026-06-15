import sys
from functools import lru_cache, cache

sys.setrecursionlimit(10 ** 8)


@cache
def F(n):
    if n > 56:
        return 1790 + F(n - 5)

    if n < 57:
        return 6 * (G(n - 7) - 31)

@cache
def G(n):
    if n < 221440:
        return -3 + G(n + 13)

    if n > 221439:
        return 52 + n / 60

for x in range(2000):
    G(x)




print(F(1614))