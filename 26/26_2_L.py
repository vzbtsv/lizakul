f = open('/Users/elizavetakulesova/Downloads/26_6056.txt')
n = f.readline()
s = []
for line in f:
    s.append(int(line))
idx = s.index(max(s))
ans = 0
# l = 0
maxi = 0
s2 = s[::-1]
# print(s)
# print(max(s2))
idx = len(s) - 1 - s2.index(max(s))
# print(s[idx])
# print(s2[idx], s[len(s) - 1 - idx])
# print(idx)
maxi = s[idx] * (idx + 1)
while len(s) > 0:
    ans += s[idx] * (idx + 1)
    s = s[idx + 1:]
    s2 = s[::-1]
    if len(s2) == 0:
        break
    idx =  len(s2) - 1 - s2.index(max(s2))
print(ans, maxi)
