import random

n = int(input())
lst = list(map(int, input().split()))

def lomuto(lst):
    l_i = 0
    m = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < m:
            l_i += 1
            lst[l_i], lst[i] = lst[i], lst[l_i]
    if l_i > 0:
        lst[0], lst[l_i] = lst[l_i], lst[0]
    return lst

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    m = lst[random.randint(0, len(lst)-1)]
    ind = lst.index(m)
    lst[0], lst[ind] = lst[ind], lst[0]
    llst = lomuto(lst)
    ind = lst.index(m)
    lst_small = llst[:ind]
    lst_big = llst[ind + 1:]
    sort_list_sm = quick_sort(lst_small)
    sort_list_bg = quick_sort(lst_big)
    mlist = [m]
    sort_lst = sort_list_sm + mlist + sort_list_bg
    return sort_lst

sorted_lst = quick_sort(lst)
print(*sorted_lst)