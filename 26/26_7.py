f = open("26_2254.txt").readlines()


n, val = list(map(int, f[0].split()))


data = sorted([[int(i) if i not in "QZ" else i for i in x.split()] for x in f[1:]], key=lambda x: (x[1], x[0]))
res = []


for x in data:
    price, type_of_product = x

    if len(res) < 95:
        res.append(x)
        val -= price

    else:
        break

print(res)
zets = list(filter(lambda x: x[1] == "Z", data))


for i in zets:
    if val >= 0:
        break

    exp = res.pop(-1)
    res = [i] + res
    val += (exp[0] - i[0])


print(res)
print(len(res))
ques = list(filter(lambda x: x[1] == "Q", res))
zets = list(filter(lambda x: x[1] == "Z", res))

print(len(ques))
print(val)