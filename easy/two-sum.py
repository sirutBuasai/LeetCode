class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_d = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in complement_d.keys():
                return [complement_d.get(complement), index]
            else:
                complement_d[value] = index
