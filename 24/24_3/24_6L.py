from re import *

f = open('/Users/elizavetakulesova/Downloads/24_7981.txt').read()
cnt = 0
f_slo = r'(?:[A-Z][a-z]*)'
slo = r'(?:[a-z]{1,})'
pat = rf'{f_slo}(?: {slo})*)\.'
res = findall(pat, f)
print(res)