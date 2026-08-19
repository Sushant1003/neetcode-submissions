class Solution:
    def trap(self, h: List[int]) -> int:
        l = [0]*len(h)
        curl = 0
        for i in range(1, len(h)):
            l[i] = max(h[i-1], curl)
            curl = max(curl, l[i])
        r = [0]*len(h)
        curr = 0
        for i in range(len(h)-2, -1, -1):
            r[i] = max(h[i+1], curr)
            curr = max(curr, r[i])
        ans =0
        for i in range(len(h)):
            ans += max((min(l[i],r[i])-h[i]),0)
        return ans