class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []
        self.min_val = float('inf')


    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_val:
            self.min_list.append(self.min_val)
            self.min_val = val


    def pop(self) -> None:
        if self.stack[-1] == self.min_val:
            self.min_val = self.min_list[-1]
            self.min_list = self.min_list[:-1]
        self.stack = self.stack[:-1]


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_val
