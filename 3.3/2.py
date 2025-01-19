n, m = input().split()
n = int(n)
m = int(m)
if abs(n - m) % 3 == 0 or n == m:
    print("Lose")
else:
    print("Win")