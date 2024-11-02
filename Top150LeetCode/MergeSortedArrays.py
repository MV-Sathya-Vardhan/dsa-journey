"""
Link to problem: 
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # Two pointer approach
    idx1,idx2 = 0,0

    # loop till end of the smaller array
    while(idx2 < n):
        # for each element in nums2, iterate nums1 till m or we find the element which is greater than current element of nums2
        while(idx1 < m and nums1[idx1] <= nums2[idx2]): 
            idx1 += 1
        nums1.insert(idx1,nums2[idx2]) # insert element from nums2 to nums1.
        nums1.pop(-1) # pop the last 0
        # increment the pointers
        idx1 += 1 
        idx2 += 1
        m += 1 # since the length of nums1 is also changed we need to handle the side effect.