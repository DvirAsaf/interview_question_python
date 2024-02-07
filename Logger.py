'''
359. Logger Rate Limiter
 Designs a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at almost every 10 seconds
(i.e., a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10)

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message)
Returns true if the message should be printed in the given timestamp, otherwise returns false.
'''
import collections


class Logger:
    # in this approach, we use a dictionary, and we don't actually delete any items.
    # this saves us some runtime and runs smoother.
    def __init__(self):
        self._dct = collections.defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # if the message wasn't in the dictionary to begin with, add it with the current
        # timestamp and return True because it is to be printed now
        if message not in self._dct:
            self._dct[message] = timestamp
            return True
        # if the message we got is a duplicate of an expired message, 'update' its timestamp
        if timestamp - self._dct[message] >= 10:
            self._dct[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated, and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
