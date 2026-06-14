from re import *

f = open('24_21161.txt').read()
cnt = 0
f_slo = r'(?:[A-Z][a-z]*)'
slo = r'(?:[a-z]+)'
pat = rf'{f_slo}(?: {slo}|{f_slo})*\.'
res = findall(pat, f)
print(len(max(res, key=len)))