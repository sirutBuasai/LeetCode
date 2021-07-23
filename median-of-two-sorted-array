class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_total = nums1 + nums2
        nums_total.sort()
        
        n = len(nums_total)
        mid_index = (n // 2)
        sum = 0
        
        if (n % 2) == 0:
            upper_median = nums_total[mid_index]
            lower_median = nums_total[mid_index -1]
            
            sum = (upper_median + lower_median) / 2
        
        else:
            sum = nums_total[mid_index]
            
        return sum
        
