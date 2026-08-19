class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Case
        if len(nums) == 0:
            return [[]]
        # Recursion
        arr = self.permute(nums[1:]) 
        # Assuming arr somehow has permutations of next stage: [[2,3],[3,2]]
        # All i need to do are add new permutations in current stage
        res = []
        for p in arr: # let p be [2,3] 
            for i in range(len(p) + 1): # Note i take 0 to n+1; Let i = 0
                p_ = p.copy() # p_ = [2,3] 
                p_.insert(i, nums[0]) # p_ = [1,2,3]
                res.append(p_) # [[1,2,3]]
        return res
        