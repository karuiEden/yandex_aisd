import math
n,k = input().split()
n = int(n)
k = int(k)
ans = math.floor(math.factorial(n+k-1) / (math.factorial(k) * math.factorial(n-1)))
print(ans)