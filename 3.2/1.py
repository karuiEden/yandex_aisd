n = int(input())
itr = []
for i in range(n):
    l, r = input().split()
    if itr.count((int(l), int(r))) == 0:
        itr.append((int(l), int(r)))
itr.sort(key=lambda x: x[1])
n = len(itr)
for i in range(n):
    if len(itr) == 0:
        break
    j = i + 1
    while j < len(itr):
        if itr[j][0] <= itr[i][1] <= itr[j][1]:
            del itr[j]
            continue
        j += 1
print(len(itr))