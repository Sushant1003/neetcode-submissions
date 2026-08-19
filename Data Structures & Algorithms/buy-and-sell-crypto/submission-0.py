class Solution:
    def maxProfit(self, p: List[int]) -> int:
        curp = 0
        maxp = 0
        buy = 0
        n = len(p)
        for i in range(n):
            if p[i]<=p[buy]:
                buy = i
            else:
                curp = p[i] - p[buy]
                maxp = max(maxp,curp)
        return maxp
