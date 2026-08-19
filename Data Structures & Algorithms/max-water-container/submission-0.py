class Solution:
    def maxArea(self, h: List[int]) -> int:
        mv, cv = 0, 0
        l, r = 0, len(h)-1
        while(l<r):
            cv = min(h[l], h[r]) * (r-l)
            mv = max(cv, mv)
            if h[l]>=h[r]:
                r-=1
            else:
                l+=1
        return mv