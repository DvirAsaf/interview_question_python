# minimum moves for all elements in array to be equals
# each move is increase/decrease by one


def min_cost(arr):
    n = len(arr)
    cost = 0
    arr.sort()
    k = arr[n // 2]
    for i in range(n):
        cost += abs(arr[i] - k)

    if n % 2 == 0:
        temp = 0
        k = arr[(n // 2) - 1]
        for i in range(n):
            temp += abs(arr[i] - k)
        cost = min(cost, temp)

    return cost


if __name__ == '__main__':
    print(min_cost([6,6,6,6,3,2,1,9,4]))
