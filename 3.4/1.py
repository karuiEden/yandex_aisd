n = int(input())

def hanoiQuantity(n):
    if n == 1:
        return 1
    return 2*hanoiQuantity(n-1)+1

print(hanoiQuantity(n))

def hanoi(n, fromTow, toTow):
    if n == 1:
        print(f'{fromTow} {toTow}')
        return
    unusedTow = 6 - fromTow - toTow
    hanoi(n-1, fromTow, unusedTow)
    print(f'{fromTow} {toTow}')
    hanoi(n-1, unusedTow, toTow)
hanoi(n, 1, 3)
