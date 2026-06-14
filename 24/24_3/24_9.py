import re


f= open("24_17878.txt").read()
number = r'(?:[1-9][0-9]*|0)'
pat = rf'{number}(?:[-*]{number})*'

res = re.findall(pat, f)

print(max(res, key=len))
print(len(max(res, key=len)))