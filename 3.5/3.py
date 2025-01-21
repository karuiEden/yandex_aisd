n = int(input())
lst = list(map(int, input().split()))

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

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    half = len(lst) // 2
    fh = lst[0:half]
    sh = lst[half + 1::]
    sort_fh = merge_sort(fh)
    sort_sh = merge_sort(sh)
    sort_lst = merge(sort_fh, sort_sh)
    return sort_lst
sort_list = merge_sort(lst)
print(*sort_list)