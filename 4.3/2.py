n = int(input())
v = float(1 + (n-2) * 2)
if 1.5*n >= v:
    print("No")
else:
    print("Yes")
    a = list()
    a.append(n)
    for i in range(1, n):
        a.append(i+1)
    print(*a)