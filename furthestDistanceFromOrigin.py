"""
2833. The furthest Point From Origin
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'.
The string represents your movement on a number line starting from origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.
"""


def furthest_distance_from_origin(self, moves: str) -> int:
    best = 0

    for dx in [-1, 1]:
        current = 0
        for move in moves:
            if move == 'L':
                current -= 1
            elif move == 'R':
                current += 1
            else:
                current += dx
        best = max(best, abs(current))
    return best
