f = open('/Users/elizavetakulesova/Downloads/24_1255.txt').read()
s = []
ans = 0
for line in f:
    if line.count('A') < 25:
        alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for el in alf:
            if el not in line:
                continue
            b = line.index(el)
            st = line[::-1]
            c = st.index(el)
            c = len(st) - 1 - c
            ans = max(ans, c - b)
print(ans)