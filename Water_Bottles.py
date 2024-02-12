"""
1518. Water Bottles
There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 15 + 3 + 1 = 19.
"""


def num_water_bottles(self, numBottles: int, numExchange: int) -> int:
    # first we count all the full bottles
    result = numBottles
    # second, we continue to decrease the battles that we drink,
    # but in each iteration we decrease 'numExchange' of empty bottles but minus 1.
    # this is because : for every 'numExchange' empty bottles we get new full bottle.
    while numBottles >= numExchange:
        numBottles -= numExchange - 1
        result += 1
    return result
