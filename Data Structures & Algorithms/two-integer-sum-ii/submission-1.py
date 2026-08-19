class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            y = self.search(target-nums[x], nums, x+1, len(nums)-1)
            if y!= -1:
                return [x+1,y+1]
        # return self.search(2,nums,0,3)
    def search(self, n, nums, i, j):
        if i<=j:
            m = (i+j)//2
            if n<nums[m]:
                return self.search(n, nums, i, m-1)
            elif n>nums[m]:
                return self.search(n,nums,m+1,j)
            elif n == nums[m]:
                return m
        return -1
        
        