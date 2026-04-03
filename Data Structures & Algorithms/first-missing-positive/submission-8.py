class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = max(nums[i], 0)
        for n in nums:
            if n > len(nums):
                continue
            if n == 0: continue
            nums[abs(n) - 1] = abs(nums[abs(n) - 1]) * -1 if abs(nums[abs(n) - 1]) != 0 else -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1