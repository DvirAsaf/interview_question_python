"""
1029. Two City Scheduling
 companies are planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti],
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""
from typing import List


def two_city_sched_cost(self, costs: List[List[int]]) -> int:
    """
    we must send n people to city A and n pepole to city B
    we should sort the array costs by the different between the a_cost_i to b_cost_i
    when the smaller different first, the first n people will be sent to A,
    the other n people will send to B, with the bigger differnt
    """
    costs.sort(key=lambda x: x[0] - x[1])
    total = 0
    n = len(costs) // 2
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    return total
