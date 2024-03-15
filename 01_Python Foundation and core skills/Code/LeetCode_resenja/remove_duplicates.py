class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
solution = Solution()
A = [0,0,1,1,5,6]
print(solution.removeDuplicates(A))


class Solution2:
    def removeDuplicates2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        l = []
        for element in nums:
            if element not in l:
                l.append(element)
        return int(len(l))

solution2 = Solution2()
A2 = [0,0,1,1,5,6]
print(solution2.removeDuplicates2(A2))