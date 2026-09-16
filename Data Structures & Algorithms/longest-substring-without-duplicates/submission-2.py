class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            if (s[right] in seen.keys() and seen[s[right]]>=left):
                left = seen[s[right]] + 1
            ans = max(right - left + 1, ans)
            seen[s[right]] = right
        return ans