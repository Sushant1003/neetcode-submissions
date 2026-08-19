class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starters = set()
        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                starters.add(nums[i])
        if not nums:
            return 0
        ml = 1
        for i in starters:
            cl = 1
            while i+1 in seen:
                cl += 1
                ml = max(cl,ml)
                i += 1
        return ml
