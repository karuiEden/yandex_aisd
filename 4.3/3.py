n = int(input())
a = list(map(int, input().split()))
a.sort()
max1 = a[n-4] * a[n-3] * a[n-2] * a[n-1]
max2 = a[n-1] * a[n-2] * a[n-3] * a[0]
max3 = a[n-1] * a[n-2] * a[1] * a[0]
max4 = a[n-1] * a[2] * a[1] * a[0]
max5 = a[0] * a[1] * a[2] * a[3]
print(max(max1, max2, max3, max4, max5))