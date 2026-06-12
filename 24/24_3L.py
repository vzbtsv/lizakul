f = open('/Users/elizavetakulesova/Downloads/24_9753.txt').read()
s = f.split('Y')
maxi = 0
for i in range(len(s) - 151):
    st = 'Y'.join(s[i:i + 151])
    maxi = max(maxi, len(st))
print(maxi)