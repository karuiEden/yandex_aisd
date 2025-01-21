n = int(input())
lst = list(map(int, input().split()))
def lomuto(lst):
    l_i = 0
    m = lst[0]
    for i in range(1,n):
        if lst[i] < m:
            l_i += 1
            lst[l_i], lst[i] = lst[i], lst[l_i]
    if l_i > 0:
        lst[0] = lst[l_i]
        lst[l_i] = m
    return lst
lom = lomuto(lst)
print(*lom)