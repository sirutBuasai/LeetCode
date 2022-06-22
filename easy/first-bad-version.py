class Solution:
    def firstBadVersion(self, n):
      l = 0
      r = n
      while l < r:
        m = ((r-l)//2) + l
        if isBadVersion(m):
          r = m
        else:
          l = m+1

      return l
