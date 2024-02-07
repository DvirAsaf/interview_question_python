"""
252. Meeting Rooms
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""
from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    The idea here is to sort the meetings by starting time.
    Then, go through the meetings one by one and make sure that each meeting ends before the next one starts.
    """
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True
