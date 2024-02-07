"""
253. Meeting Rooms 2
Given an array of meeting time intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""
import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    rooms = 0
    nearest_ending = [0]
    for start, end in intervals:
        if rooms == 0:
            rooms += 1
            nearest_ending.pop()
        elif nearest_ending[0] > start or nearest_ending[0] == end:
            rooms += 1
        else:
            nearest_ending[0] = nearest_ending[-1]
            nearest_ending.pop()
        nearest_ending.append(end)
        heapq.heapify(nearest_ending)

    return rooms
