class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        # cur = ""
        def dfs(i,cur):
            if i >= len(digits):
                res.append(cur[::])
                return

            for ch in mapping[digits[i]]:
                # cur += ch
                dfs(i+1,cur+ch)
                # cur.replace(ch,"")
        if digits:
            dfs(0,"")
        
        # res = []
        # res.append(int(digits[0]))
        return res