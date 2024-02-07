"""
362. Design Hit Counter
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity),
and you may assume that calls are being made to the system in chronological order (i.e.,
timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter-system.
Void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
Several hits may happen at the same timestamp.
Int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""


class HitCounter:

    def __init__(self):
        # the first value is representing the time stamp,
        # the second value is representing the count of hits in the same time stamp
        self.hits = [(0, 0)] * 300

    def hit(self, timestamp: int) -> None:
        # when we get hit, first we need to find which time the hit upper, fot that we module by 300
        i = (timestamp - 1) % 300
        # now we take from tuple array hits above the respectively tuple, if there is not a tuple fit to i we get (0, 0)
        t, c = self.hits[i]

        if timestamp - t < 300:
            self.hits[i] = (timestamp, c + 1)
        else:
            self.hits[i] = (timestamp, 1)

    def getHits(self, timestamp: int) -> int:
        count = 0
        for t, c in self.hits:
            if timestamp - t < 300:
                count += c

        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
