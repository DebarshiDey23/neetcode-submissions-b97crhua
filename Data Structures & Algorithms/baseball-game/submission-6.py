class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for o in operations:
            if o not in ["+", "D", "C"]:
                arr.append(int(o))
            else:
                if o == "+":
                    arr.append(arr[-1] + arr[-2])
                elif o == "D":
                    arr.append(arr[-1] * 2)
                elif o == "C":
                    arr.pop()
        return sum(arr)