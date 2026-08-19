class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,sub,total):

            if target == total:
                res.append(sub.copy())
                return
            if target<total or i >= len(candidates):
                return
            
            
            
            #include element
            sub.append(candidates[i])
            dfs(i+1,sub,total+candidates[i])
            sub.pop()
            #exclude element
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1,sub,total)
        dfs(0,[],0)
        return res