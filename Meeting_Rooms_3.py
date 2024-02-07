"""
2402. Meeting Rooms 3
You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [starti, endi]
means that a meeting will be held during the half-closed time interval [starti, endi).
All the values of starti are unique.
Meetings are allocated to rooms in the following manner:
Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free.
The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the amount of the room that held the most meetings. If there are multiple rooms,
return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: Zero
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finish. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held two meetings, so we returned 0.
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: One
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held two meetings, so we return 1.
"""
import heapq
from typing import List


# approach: priority queue, implemented using min heap
def most_booked(n: int, meetings: List[List[int]]) -> int:
    # for rooms that are available
    unoccupied = [room for room in range(n)]
    # initializing an empty list for rooms that'll be in use
    occupied = []
    # converting the unoccupied rooms list into a heap
    heapq.heapify(unoccupied)
    # initializing a list for the number of times, each room gets booked
    booking_counts = [0] * n

    # sort meetings. ascending, according to first element (start time)
    srted = sorted(meetings, key=lambda x: x[0])
    for start, end_time in srted:
        # occupied[0] = first element in occupied. occupied[0][0] = end time of a first element of occupied
        while occupied and occupied[0][0] <= start:
            # a room becomes available, and we add it to the available rooms heap
            end, room = heapq.heappop(occupied)
            heapq.heappush(unoccupied, room)
        if unoccupied:
            # assign an available room from the heap to this meeting
            room = heapq.heappop(unoccupied)
            heapq.heappush(occupied, [end_time, room])  # adding the meeting to the occupied heap
        else:
            # if we got here, that means all rooms are occupied.
            # therefore, we find the room with the earliest end time. we use pop bc it's a minheap
            cur_end, room = heapq.heappop(occupied)
            new_end = cur_end + end_time - start  # update the rooms end time
            heapq.heappush(occupied, [new_end, room])
        booking_counts[room] += 1

    # now we'll find the room with the max booking counts
    max_bookings = max(booking_counts)
    most_book = booking_counts.index(max_bookings)
    return most_book
