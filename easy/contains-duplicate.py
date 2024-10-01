class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for n in nums:
          if n in d.keys():
            return d[n]

          else:
            d[n] = True

        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for n in nums:
          if n in s:
            return True

          else:
            s.add(n)

        return False
