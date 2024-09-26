class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None


    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        x = self.s1.pop()

        if self.s1:
            self.front = self.s1.pop()
            self.s2.append(self.front)

            while self.s1:
                self.s2.append(self.s1.pop())

            while self.s2:
                self.s1.append(self.s2.pop())
        else:
            self.front = None

        return x


    def peek(self) -> int:
        return self.front


    def empty(self) -> bool:
        return False if self.s1 else True
