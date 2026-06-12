import re

f = open("24_4555.txt").read()
pat = r"(?:XY|ZZX)*"
res = re.findall(pat, f)
print(len(max(res, key=len)))