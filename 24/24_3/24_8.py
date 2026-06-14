import re

f = open("24_18619.txt").read()

number = r"(?:[1-9][0-9]*|0)"
equation = rf"{number}(?:[-*]{number})*"
pat = rf"B+{equation}"


res = re.findall(pat, f)

print(max(res, key=len))
print(len(max(res, key=len)))