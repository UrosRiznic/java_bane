class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_str = str(x)
        if temp_str == temp_str[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(121))