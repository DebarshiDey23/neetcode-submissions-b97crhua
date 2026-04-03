class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rPointer = len(nums) - 1
        lPointer = mPointer = 0
        while mPointer <= rPointer:
            if nums[mPointer] == 0:
                nums[lPointer], nums[mPointer] = nums[mPointer], nums[lPointer]
                lPointer += 1
                mPointer += 1
            elif nums[mPointer] == 2:
                nums[rPointer], nums[mPointer] = nums[mPointer], nums[rPointer]
                rPointer -= 1
            else:
                mPointer += 1