"""
Link to problem: 
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
    1.  Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
        The remaining elements of nums are not important as well as the size of nums.
    2.  Return k.

"""

def removeElement(nums: List[int], val: int) -> int:
    # loop through the list and pop the element which is equal to val.
    # return the length of array once all elements equal to val are popped out.
    idx = 0
    while idx < len(nums):
        if nums[idx] == val:
            nums.pop(idx)
        else: 
            idx += 1
    return len(nums)
