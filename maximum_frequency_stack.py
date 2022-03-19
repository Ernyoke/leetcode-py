# https://leetcode.com/problems/maximum-frequency-stack

import collections


class FreqStack:

    def __init__(self):
        self._stack = collections.defaultdict(list)
        self._counter = collections.Counter()
        self._max_freq = 0

    def push(self, val: int) -> None:
        self._counter[val] += 1
        self._max_freq = max(self._max_freq, self._counter[val])
        self._stack[self._counter[val]].append(val)

    def pop(self) -> int:
        ans = self._stack[self._max_freq].pop()
        self._counter[ans] -= 1
        if len(self._stack[self._max_freq]) == 0:
            self._max_freq -= 1
        return ans


if __name__ == '__main__':
    freq_stack = FreqStack()
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(4)
    freq_stack.push(5)

    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())

    freq_stack_2 = FreqStack()
    freq_stack_2.push(4)
    freq_stack_2.push(0)
    freq_stack_2.push(9)
    freq_stack_2.push(3)
    freq_stack_2.push(4)
    freq_stack_2.push(2)
    print(freq_stack_2.pop())
    freq_stack_2.push(6)
    print(freq_stack_2.pop())
    freq_stack_2.push(1)
    print(freq_stack_2.pop())
    freq_stack_2.push(1)
    print(freq_stack_2.pop())
    freq_stack_2.push(4)
    print(freq_stack_2.pop())
    print(freq_stack_2.pop())
    print(freq_stack_2.pop())
    print(freq_stack_2.pop())
    print(freq_stack_2.pop())
    print(freq_stack_2.pop())
