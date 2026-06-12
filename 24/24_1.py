import re

f = open("24_12476.txt").read()

# pat = r"[PROEG]*(?:(?:RO)[PROEG]*){21}"
#
# res = re.findall(pat, f)
#
#
# print(max(res, key=len))


f = f.split("RO")
maxx = "0"
for i in range(len(f) - 1):
    st = "RO".join(f[i:i + 22])
    if "ORO" not in st and "ROR" not in st:
        maxx = max(maxx, st, key=len)

print(maxx.count("RO"))
print(len(maxx))

