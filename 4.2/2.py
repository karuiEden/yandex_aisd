n = int(input())
a = list(map(int, input().split()))
a.reverse()
m = int(input())
b = list(map(int, input().split()))
b.reverse()

for i in range(min(n,m) + 1):
    a[i] += b[i]
print(max(n,m))
a.reverse()
print(*a)