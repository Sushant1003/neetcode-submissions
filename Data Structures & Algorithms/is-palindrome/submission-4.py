class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for ch in s:
            if (ord('a') <= ord(ch) <= ord('z')) or (ord('A') <= ord(ch) <= ord('Z')):
                temp += ch.lower()
            elif (ord('0') <= ord(ch) <= ord('9')):
                temp += ch
        return temp == temp[::-1]