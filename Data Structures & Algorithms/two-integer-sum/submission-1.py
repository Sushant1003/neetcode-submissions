class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        ans = []
        for i in range(len(nums)):
            a[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in a.keys() and i!=a[target - nums[i]]:
                ans.append(i)
                ans.append(a[target - nums[i]])
                return ans

                