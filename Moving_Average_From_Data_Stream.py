"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]
Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
"""
import collections


class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.total = 0
        self.counter = 0
        self.size = size
        for i in range(size):
            self.queue.append(0)

    def next(self, val: int) -> float:
        self.counter += 1
        right = self.queue.popleft()
        self.queue.append(val)
        self.total = self.total - right + val
        if self.counter < self.size:
            return float(self.total / self.counter)
        return float(self.total / self.size)
    