import math
n,k = input().split()
n = int(n)
k = int(k)
def fact(a):
    ans = 1
    for i in range(1, a+1):
        ans = ans * i
    return ans
fact_n = fact(n)
fact_k = fact(k)
fact_nk = fact(n-k)
ans = math.floor(fact_n / (fact_k * fact_nk))
print(ans)