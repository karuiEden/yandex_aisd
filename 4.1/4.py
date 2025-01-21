m, n = input().split()
m = int(m)
n = int(n)

def matrix(m, n):
    mtr = list()
    for i in range(m):
        mtr.append(list(map(int, input().split())))
    return mtr
a = matrix(m,n)
b = matrix(m,n)
for i in range(m):
    for j in range(n):
        a[i][j] += b[i][j]
for i in range(m):
    print(*a[i])