from pstats import SortKey

f = open("24_1148.txt").readlines()
f2 = open("24_1148.txt").read()

d = sorted(f, key=lambda x: x.count("Q"))

d = f[-1]


alp = "qwertyuiopasdfghjklzxcvbnm".upper()

res = []
for a in alp:
    res.append((f.count(a), a))

print(f2.count("C"))
print(min(res))

