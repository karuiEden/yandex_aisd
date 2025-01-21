n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    min_v = min(lst[i::])
    if min_v == lst[i]:
        continue
    min_i = lst.index(min_v)
    temp = lst[i]
    lst[i] = min_v
    lst[min_i] = temp
print(*lst)