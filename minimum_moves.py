# minimum moves for array to be from 1 to n
# each move is increase/decrease by one


def min_moves(arr):
    n = len(arr)
    moves = 0
    arr.sort()
    for i in range(n):
        moves += abs(arr[i] - (i + 1))
    return moves


if __name__ == '__main__':
    print(min_moves([6,6,6,6,3,2,1,9,4]))
