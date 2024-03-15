class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSumDict(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for key, value in enumerate(nums):
            if target - value in seen:
                return([seen[target-value], key])
            elif value not in seen:
                seen[value] = key

s1 = Solution()
l = [3,3]
t = 6
print(s1.twoSum(l,t))
print(s1.twoSumDict(l,t))

