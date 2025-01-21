import sys

n = int(input())
lst_lst = list()
for i in range(n):
    buf = input()
    lst_lst.append([int(x) for x in sys.stdin.readline().split() ])

def merge(lst1, lst2):
    mlst = list()
    i, j = 0, 0
    while len(lst1) > i and len(lst2) > j:
        if lst1[i] < lst2[j]:
            mlst.append(lst1[i])
            i += 1
        else:
            mlst.append(lst2[j])
            j += 1
    if len(lst1) > i:
        mlst.extend(lst1[i:])
    else:
        mlst.extend(lst2[j:])
    return mlst
ans = lst_lst[0]
for i in range(1,n):
    ans = merge(ans, lst_lst[i])
print(*ans)