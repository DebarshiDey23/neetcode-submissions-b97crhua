class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = [(i, abs(i - x)) for i in arr]
        lst.sort(key = lambda x: (x[1], x[0]))
        return sorted([i[0] for i in lst[:k]])