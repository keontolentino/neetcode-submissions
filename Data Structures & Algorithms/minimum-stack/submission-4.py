class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_num:
            self.min_num.append(val)
        else:
            self.min_num.append(min(val, self.min_num[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
