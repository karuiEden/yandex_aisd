n = int(input())
a = list(map(int, input().split()))
a.sort()
max1 = a[n-4] * a[n-3] * a[n-2] * a[n-1]
max2 = a[n-1] * a[n-2] * a[0] * a[1]
print(max(max1, max2))