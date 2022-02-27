# https://leetcode.com/problems/3sum-closest/submissions/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        s = nums[0] + nums[1] + nums[2]
        min_sum = abs(target - s)
        res = s
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if min_sum > abs(target - s):
                    min_sum = abs(target - s)
                    res = s
                if s < target:
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest([1, 1, 1, 0], -100))
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest(
        [-93, -78, -7, 50, 17, 62, -17, 25, -10, 22, 74, 1, 80, 94, 5, -42, 25, 30, -45, -28, 54, 1, -56, -10, 58, -88,
         -45, 0, -6, -93, -76, 76, 19, 66, 52, 25, 84, -42, 86, 38, 50, 40, 81, 87, -1, -97, 80, -44, -11, -96, -71,
         -35, 13, 26, 96, 7, -22, -73, 21, -88, -4, -65, 23, -48, 86, 63, 98, 76, 7, 76, -100, 46, -29, -57, -44, 38,
         28, -98, 79, -17, -22, -86, -10, 96, -29, -52, -53, 16, 84, 99, 83, -8, -5, 95, -84, -80, -59, 91, 59, -53, 23,
         -49, -69, 24, -70, -12, -24, 29, 58, -12, -36, -13, -90, 29, -57, 35, 53, -89, 81, -73, 67, -68, -37, -53, 21,
         2, -24, -17, -53, 95, -28, 21, 45, 0, -54, -7, 23, -78, 38, 55, -62, -48, 5, -32, 11, 33], 48))
