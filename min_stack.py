# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, val: int) -> None:
        self.min_value = val if self.min_value is None else min(self.min_value, val)
        self.stack.append((val, self.min_value))

    def pop(self) -> None:
        self.stack.pop()
        self.min_value = None if len(self.stack) == 0 else self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    stack.pop()
