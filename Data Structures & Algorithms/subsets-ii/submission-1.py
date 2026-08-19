class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur[::])
                return
            # Include element
            cur.append(nums[i])
            dfs(i+1)
            cur.remove(nums[i])
            # Don't include the element
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res

        # nums.sort()
        # res = []
        # def dfs(i, cur):
        #     if i >= len(nums):
        #         res.append(cur[::])
        #         return
        #     # Include element
        #     cur.append(nums[i])
        #     dfs(i+1,cur)
        #     cur.remove(nums[i])
        #     # Don't include the element
        #     while i+1<len(nums) and nums[i+1] == nums[i]:
        #         i+=1
        #     dfs(i+1,cur)
        # dfs(0,[])
        # return res
        