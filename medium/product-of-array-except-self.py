class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num0 = 0
        idx0 = 0
        prd = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                num0 += 1
                idx0 = i
            else:
                prd *= nums[i]

        res = [0 for _ in range(len(nums))]
        if num0 == 1:
            res[idx0] = prd

        elif num0 < 1:
            for i in range(len(nums)):
                res[i] = int(prd/nums[i])

        return res
