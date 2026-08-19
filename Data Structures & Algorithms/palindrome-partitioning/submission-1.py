class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # cur = ""
        cur = []
        def ispal(s,i,j):
            # return s[i:j+1] == s[j:i-1:-1]
            while i<j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True

        def dfs(i):
            if i>=len(s):
                res.append(cur.copy())
                return 

            for j in range(i,len(s)):
                if ispal(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        
        # for t in res:
        #     if len(t)<1 or (not ispal(s)):
        #         res.remove(t)
        return res
                 

                

        