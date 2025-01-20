import math
def tower_of_hanoi_4pegs(n, source, aux1, aux2, target, moves):
    if n == 0:
        return
    if n == 1:
        moves.append((source, target))
        return
    k = max(1, n - int(math.sqrt(2 * n)))
    tower_of_hanoi_4pegs(k, source, target, aux2, aux1, moves)
    tower_of_hanoi_3pegs(n - k, source, aux2, target, moves)
    tower_of_hanoi_4pegs(k, aux1, source, aux2, target, moves)

def tower_of_hanoi_3pegs(n, source, auxiliary, target, moves):
    if n > 0:
        tower_of_hanoi_3pegs(n - 1, source, target, auxiliary, moves)
        moves.append((source, target))
        tower_of_hanoi_3pegs(n - 1, auxiliary, source, target, moves)


n = int(input())
moves = []
tower_of_hanoi_4pegs(n, 'A', 'B', 'C', 'D', moves)
print(len(moves))