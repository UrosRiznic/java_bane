class Solution:
    def removeElement(self, nums: list[int], val:int) -> int:
        if len(nums) == 0:
            return 0
        l = []
        for element in nums:
            if element != val:
                l.append(element)
        return int(len(nums)) - int(len(l))

s = Solution()
print(s.removeElement([3,2,2,3], 3))