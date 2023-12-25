# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for (index, num) in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            else:
                dict[num] = index

# leetcode submit region end(Prohibit modification and deletion)
