class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue
            # left is the value after val, right is the last idx
            left = idx+1
            right = len(nums) - 1
            
            while left < right:
                three_sum = val + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0: 
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
        return result
    
