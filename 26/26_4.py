

f = open("26_20828.txt").readlines()

col, rows, columns = list(map(int, f[0].split()))

matrix = [[[(0, [0, 0], 0) for x in range(columns)] for y in range(rows)] for z in range(col)]

# for i in matrix:
#     for j in i:
#         print(j)

placements = col * rows * columns

g = int(f[1])
data = sorted([list(map(int, x.split())) for x in f[2:]])
k = 0

for gruz in data:
    start, end = gruz
    passed = False
    for stellage in range(col):
        if passed:
            break
        for row in range(rows):
            if passed:
                break
            for seat in range(columns):
                if passed:
                    break
                curr_seat = matrix[stellage][row][seat]
                if curr_seat[0] == 0 or curr_seat[1][1] < start:
                    matrix[stellage][row][seat] = (1, [start, end], curr_seat[-1] + 1)
                    k += 1
                    passed = True








first = matrix[0]
print(k)
res =[]
for x in first:
    res.append(sum([y[-1] for y in x]))
    print(res)

print(res.index(min(res)))


