"""
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
from typing import List


def remove_duplicates(self, nums: List[int]) -> int:
    '''
    In this problem, we need to return array of unique values(but we can have at most 2 values that are the same).
    this addition little bit complicated the solution, the trick is to create new varable(in our example is 'count').
    we initilaze count to be -> 0,
    in addition we need 2 pointers i and j that initilaze to be -> 1.
    for better prefurmance i use addition varable 'size' for only 1 time check the len of nums
    and not in every iteration.

    '''
    count = 0
    i = 1
    j = 1
    size = len(nums)
    while i < size:
        # if 2 nearby values are not equal, we increase the pointer j accordinly.
        # and the value in nums[j] is going to be the value in nums[i].
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
            # this is in case we have before 2 nearby values that are equal and we need to reset the count to 0.
            count = 0
        else:
            # if 2 nearby values are equal we have 2 senario:
            # 1.count is less the 2 -> meaning that we can continiue we that increasing of pointer j, similary as above.
            # 2.count is 2 and above -> meaning we need to "remove" this value, we doing that by increasing pointer i,
            # and in the next iterations we meat differnt values that are going to be rewrite in the index j.
            # and the value will be change.
            count += 1
            if count < 2:
                nums[j] = nums[i]
                j += 1
        i += 1
    # finaly we return the pointer j -> meaning that the number of unique values(up to 2 values that are the same).
    return j
