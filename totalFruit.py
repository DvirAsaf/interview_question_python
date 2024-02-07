"""
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array of fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
 while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
from typing import List


def total_fruit(self, fruits: List[int]) -> int:
    n = len(fruits)  # size of all the trees (include duplicate)
    curr_type = fruits[0]  # the first fruit is curr
    curr_index = 0  # the first fruit in index 0 will contain the staring index of a sequence of fruits.
    other_type = None  # the second fruit is unknown yet
    strike = 1  # we have one fruit in a basket
    result = 0  # initialize to zero will contain the maximum fruits that we can collect from trees.
    # we iterate over the rest of the trees from 1 (second index to the end)
    for i in range(1, n):
        new_type = fruits[i]  # we put her the fruit type in the next tree(the right one)
        # if we get 2 trees that have the same fruits and the location of them is next to each other,
        # we just add one more fruit to a basket.
        if new_type == curr_type:
            strike += 1
        elif new_type == other_type:  # if the fruit type is the same as the other basket type, we change between them.
            # add 1 to the basket and mark the curr_index to this location (i)
            strike += 1
            curr_type, other_type = other_type, curr_type
            curr_index = i
        # if the fruit type is not one of the 2 types in baskets, first we need to update the maximum so far,
        # if in previous run, the result is bigger than current strike, we
        else:
            result = max(result, strike)
            # The new count (i - curr_index + 1) represents the length of the new sequence of fruits.
            strike = i - curr_index + 1  # we change the strike because we have a new sequence, that start in curr_index
            curr_index = i  # we update curr_index to start of a new sequence of fruits
            curr_type, other_type = new_type, curr_type  # we swap with the previous fruit

    result = max(result, strike)
    return result
