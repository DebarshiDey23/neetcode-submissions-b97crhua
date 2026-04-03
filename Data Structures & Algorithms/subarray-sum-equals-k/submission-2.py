class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {}
        cache[0] = 1
        running = 0
        ans = 0
        for n in nums:
            running += n
            if running - k in cache:
                ans += cache[running - k]
            cache[running] = cache.get(running, 0) + 1
        return ans