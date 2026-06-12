

f = open("26_20828.txt").readlines()

col, row, column = list(map(int, f[0].split()))

matrix = [[[0 for x in range(column)] for y in range(row)] for z in range(col)]

# for i in matrix:
#     for j in i:
#         print(j)



g = int(f[1])
data = [list(map(int, x.split())) for x in f[2:]]


for gruz in data:
    start, end = gruz





