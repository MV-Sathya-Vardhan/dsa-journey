"""
Link to problem: 
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    1.  Change the array nums such that the first k elements of nums contain the unique elements in the 
        order they were present in nums initially. The remaining elements of nums are not important as 
        well as the size of nums.
    2.  Return k.

"""

def removeDuplicates(nums: List[int]) -> int:
    # since the arrays are sorted, all duplicate elements will be stored together
    # have a current index and loop the list till current index reaches end.
    # compare numbers at current index with previous number.
    # if both are equal, pop the number at current index. otherwise,
    # update previous number to number at current index and increment current index.
    # return the length of array once all elements equal to val are popped out.
    prevNum = nums[0]
    idx = 1
    while idx < len(nums):
        if nums[idx] != prevNum:
            prevNum = nums[idx]
            idx += 1
            continue
        nums.pop(idx)
    return len(nums)
