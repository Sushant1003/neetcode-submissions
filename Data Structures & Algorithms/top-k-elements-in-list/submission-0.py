class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        i = len(freq)-1
        while k>0 and i>0:
            for n in freq[i]:
                res.append(n)
                k-=1
            i-=1
        return res