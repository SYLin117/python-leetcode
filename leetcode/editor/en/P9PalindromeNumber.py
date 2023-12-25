# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        digits = len(str(x))
        while x > 0:
            left = x // 10 ** (digits - 1)
            right = x % 10
            if left != right: return False
            x = x % (10 ** (digits - 1))
            ## IMPORTANT: x / 10 may have decimal so we need to use //
            x = x // 10
            digits -= 2
        return True


# leetcode submit region end(Prohibit modification and deletion)

Solution().isPalindrome(121)
Solution().isPalindrome(1001)
