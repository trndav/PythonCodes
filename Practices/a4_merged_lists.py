'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: int, nums2: int) -> float:

        nums1 = nums1
        nums2 = nums2

        merged = [*nums1, *nums2]
        total_sum = 0
        for num in merged:
            total_sum += num 

        average = total_sum / len(merged)

        print(average)
        return average

x = Solution()     
x.findMedianSortedArrays([2,3,4,5], [6,7,8,9])