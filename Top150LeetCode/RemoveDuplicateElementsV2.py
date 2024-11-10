"""
Link to problem: 
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that 
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the
result be placed in the first part of the array nums. More formally, if there are k elements after 
removing the duplicates, then the first k elements of nums should hold the final result. It does not 
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

"""

def removeDuplicates(nums: List[int]) -> int:
    # since the arrays are sorted, all duplicate elements will be stored together
    # have a counter "numDuplicates", current index and loop the list till current index reaches end.
    # compare numbers at current index with previous number.
    # if both are equal, check the "numDuplicates" counter, if numDuplicates = 1 pop the number at current 
    # index otherwise, increment the "numDuplicates" counter 
    # else if both numbers are not equal reset the "numDuplicates" to 0
    # update the previous number to number at current index and increment current index.
    # return the length of array once all elements equal to val are popped out.
    prevNum = nums[0]
    idx = 1
    numDuplicates = 0
    while idx < len(nums):
        if prevNum == nums[idx]:
            if numDuplicates == 1:
                nums.pop(idx)
                continue
            else:
                numDuplicates += 1
        else:
            numDuplicates = 0
        prevNum = nums[idx]
        idx += 1
    return len(nums)

"""
Note:

This solution can be further extended to have k duplicates.
We can have an incrementor which increments each time we see a duplicate. We keep incrementing till we reach k.
upon reaching k duplicates we keep poping out the next duplicate that comes our way.

Code for having k duplicates:
    def removeDuplicates(nums: List[int], k: int) -> int:
        prevNum = nums[0]
        idx = 1
        numDuplicates = 0
        while idx < len(nums):
            if prevNum == nums[idx]:
                if numDuplicates == k:
                    nums.pop(idx)
                    continue
                else:
                    numDuplicates += 1
            else:
                numDuplicates = 0
            prevNum = nums[idx]
            idx += 1
        return len(nums)

"""