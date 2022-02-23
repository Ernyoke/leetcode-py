# https://leetcode.com/problems/slowest-key/
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        prev_duration = max_duration
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            current_duration = releaseTimes[i] - prev_duration
            if current_duration > max_duration or (current_duration == max_duration and ord(keysPressed[i]) > ord(key)):
                max_duration = current_duration
                key = keysPressed[i]
            prev_duration = releaseTimes[i]

        return key


if __name__ == '__main__':
    print(Solution().slowestKey([9, 29, 49, 50], 'cbcd'))
    print(Solution().slowestKey([12, 23, 36, 46, 62], 'spuda'))
    print(Solution().slowestKey([23, 34, 43, 59, 62, 80, 83, 92, 97], 'qgkzzihfc'))
    print(Solution().slowestKey([9, 29, 49, 50], 'cbcd'))
