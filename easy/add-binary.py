class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a,b = b,a

        a = a[::-1]
        b = b[::-1]
        carry = 0
        ans = ''

        for i in range(len(a)):
            if i < len(b):
                added = int(a[i]) + int(b[i]) + carry
            else:
                added = int(a[i]) + carry

            if added > 1:
                carry = 1
                ans += str(added % 2)
            else:
                carry = 0
                ans += str(added)


        if carry:
            ans = '1' + ans[::-1]
        else:
            ans = ans[::-1]

        return ans


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry:
            if i >=0:
                carry += int(a[i])
                i -= 1
            if j >=0:
                carry += int(b[j])
                j -= 1
            ans += str(carry % 2)
            carry //= 2

        ans = ans[::-1]
        return ans
