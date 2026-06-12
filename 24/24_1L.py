f = open('/Users/elizavetakulesova/Downloads/24_12476.txt').read()
s = f.split('RO')
ans = 0
for i in range(len(s) - 21):
    s1 = s[i:i + 22]
    st = 'RO'.join(s1)
    s2 = 'RO' + 'RO'.join(s[i + 1:i + 21]) + 'RO'
    if len(st) > ans:
        if 'ORO' in s2 or 'ROR' in s2:
            continue
        if i != 0 and i != len(s) - 22:
            st2 = 'O' + st + 'R'
        elif i != 0:
            st2 = 'O' + st
        elif i != len(s) - 22:
            st2 = st + 'R'
        if 'ORO' not in st2 and 'ROR' not in st2:
            ans = max(len(st2), ans)
            if len(st2) == 815:
                print(st2)
        elif 'ORO' not in st and 'ROR' not in st:
            ans = max(len(st), ans)
            if len(st) == 813:
                print(st)
        else:
            # continue
            st1 = s1[0][::-1]
            st2 = s1[-1]
            f1 = True
            f2 = True
            i = 0
            j = 0
            i1 = 0
            j1 = 0
            while True:
                if 'ORO' not in st1[i] + s2 and 'ROR' not in st1[i] + s2 and f1:
                    if i == len(st1) - 1 and i1 == 0:
                        s2 = 'O' + s2
                        i1 += 1
                    elif i1 > 0:
                        f1 = False
                    else:
                        s2 = st1[i] + s2
                        i += 1
                else:
                    f1 = False
                if 'ORO' not in s2 + st2[j] and 'ROR' not in s2 + st2[j] and f2:
                    if j == len(st2) - 1 and j1 == 0:
                        s2 = st2[j] + 'R'
                        j1 += 1
                    elif j1 > 0:
                        f2 = False
                    else:
                        s2 = s2 + st2[j]
                        j += 1
                else:
                    f2 = False
                if not f1 and not f2:
                    break
            ans = max(len(s2), ans)
print(ans)
