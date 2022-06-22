class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdecimal() or (len(c) > 1 and c[0] == '-'):
                stack.append(int(c))
            else:
                y,x = stack.pop(), stack.pop()
                if c == '/':
                    stack.append(int(x/y))
                elif c == '*':
                    stack.append(int(x*y))
                elif c == '+':
                    stack.append(int(x+y))
                elif c == '-':
                    stack.append(int(x-y))

        return stack.pop()
