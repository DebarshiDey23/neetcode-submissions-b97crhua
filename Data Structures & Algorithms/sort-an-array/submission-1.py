class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper(arr):
            if not arr:
                return []
            if len(arr) == 1: return arr
            left = helper(arr[:len(arr) // 2])
            right = helper(arr[len(arr) // 2:])
            ans = []
            l = r = 0
            while l < len(left) or r < len(right):
                if l == len(left):
                    ans.append(right[r])
                    r += 1
                elif r == len(right) or right[r] >= left[l]:
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            return ans
        return helper(nums)