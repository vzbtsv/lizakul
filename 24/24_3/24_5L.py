from re import *

f = open('24_7981.txt').read()
cnt = 0
ss = ['AA', 'AB', 'AC', 'BC', 'BA', 'BB', 'CC', 'CA', 'CB']
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        st = f[i:j + 1]
        if f[i] == f[j]:
            if ('AA' not in f[i:j + 1] and 'AB' not in f[i:j + 1] and 'AC' not in f[i:j + 1] and 'BB' not in f[
                                                                                                             i:j + 1] and 'BA' not in f[
                                                                                                                                      i:j + 1] and 'BC' not in f[
                                                                                                                                                               i:j + 1] and 'CC' not in f[
                                                                                                                                                                                        i:j + 1] and 'CA' not in f[
                                                                                                                                                                                                                 i:j + 1] and 'CB' not in f[i:j + 1]):
                cnt += 1
            else:
                break

print(cnt)
