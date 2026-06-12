

f = open("26_13292.txt").readlines()

n, k = list(map(int, f[0].split()))

save = [0 for i in range(k)]

data = sorted([int(x) for x in f[1:]])
summ = 0
last = 0
for x in data:
    if x % 2 == 0:
        for i in range(k):
            if save[i] == 0:
                save[i] = x
                print(i + 1)
                last_i = i
                break

    else:
        for i in range(k - 1, -1, -1):
            if save[i] == 0:
                save[i] = x
                print(i + 1)
                summ += x
                last_i = i
                break


save = list(filter(lambda x: x % 2 != 0, save[last_i + 1:]))
print(sum(save))

