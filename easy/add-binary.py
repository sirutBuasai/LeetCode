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
