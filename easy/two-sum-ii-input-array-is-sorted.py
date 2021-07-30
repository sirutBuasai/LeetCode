class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lo = 0
        hi = len(numbers)-1

        while lo < hi:
          added = numbers[lo] + numbers[hi]
          
          if added > target:
            hi -= 1

          elif added < target:
            lo += 1

          else:
            return[lo+1, hi+1]
          
