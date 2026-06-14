import re

f = open("24_21161.txt").read()
sentence = r"[A-Z][a-z]*(?:[ ][A-Z]?[a-z]+)*[.]"
res = re.findall(sentence, f)
print(len(max(res, key=len)))
