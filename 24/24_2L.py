f = open('/Users/elizavetakulesova/Downloads/24_1148.txt')
s = []
maxi = -1
spc = []
for line in f:
    spc.append(line[:-1])
    maxi = max(maxi, line.count('Q'))
    if line.count('Q') == 64:
        s.append(line[:-1])
st = s[0]
dct = dict()
for el in st:
    if el not in dct:
        dct[el] = 1
    else:
        dct[el] += 1
mini = 10 ** 10
for el in dct:
    if dct[el] < mini:
        mini = dct[el]
    if dct[el] == 22:
        print(el)
st = ''.join(spc)
print(st.count('C'))