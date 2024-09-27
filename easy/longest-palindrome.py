class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        length = 0
        odd = False

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for k in d.keys():
            if d[k] % 2 == 0:
                length += d[k]
            elif d[k] > 1:
                length += d[k]-1
                odd = True

        return length+1 if odd else length


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = set()
        length = 0

        for c in s:
            if c in d:
                d.remove(c)
                length += 2
            else:
                d.add(c)

        return length+1 if d else length
