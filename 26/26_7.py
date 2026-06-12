

f = open("26_2254.txt").readlines()


n, val = list(map(int, f[0].split()))


data = sorted([[int(i) if i not in "QZ" else i for i in x.split() ] for x in f[1:]], key=lambda x: (x[1], x[0]))
res = []

for x in data:
    price, state = x
    if val - price >= 0:
        res.append(x)
        val -= price

    else:


print(len(res))
print(res)
print(val)









