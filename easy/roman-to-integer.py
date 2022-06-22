class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ans = 0

        # Iterate from index 0 to second last index. We do this to avoid index out of range.
        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]

        # Always add last roman number in the string as the last index is not accounted for in the loop.
        return ans + roman_dict[s[-1]]
