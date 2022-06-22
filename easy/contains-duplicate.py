class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for n in nums:
          if n in d.keys():
            return d[n]

          else:
            d[n] = True

        return False
