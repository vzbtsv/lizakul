

def is_palindrome(x):
    return x == x[::-1]



f = open("24_1761.txt").read()

maxx = 0
for i in range(len(f)):
    for j in range(len(f), i + maxx - 1, -1):
        st = f[i:j]

        if is_palindrome(st):
            maxx = max(len(st), maxx)
            print(maxx)
            break
print(maxx)