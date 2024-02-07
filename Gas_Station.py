# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank, and it costs[i] of gas to travel from the ith station to its next
# (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
# the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
# it is guaranteed to be unique.
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    # the trick is to traversal over gas and cost, and for every iteration if gas[i] - cost[i] < 0
    # so we cant continue moving, so we need to check the staring point in i + 1 index.
    total_gain = 0  # total_gain is to check if we can traversal over the road from any staring point.
    current_gain = 0  # current_gain is to check if the starting point has enough gas for all trips
    answer = 0  # the answer is the index of starting point, if their Solution

    for i in range(len(gas)):
        total_gain += gas[i] - cost[i]
        current_gain += gas[i] - cost[i]
        # If we meet a "valley", start over from the next station with 0 initial gas.
        if current_gain < 0:
            current_gain = 0
            answer = i + 1

    return answer if total_gain >= 0 else -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    answer = can_complete_circuit(gas, cost)
    print(answer)
