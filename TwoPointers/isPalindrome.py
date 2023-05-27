class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""


        for i in range(len(s)):
            if s[i].isalnum():
                s_clean += s[i]
        
        print(s_clean)
        s_clean = s_clean.lower()
        n = len(s_clean)
        for i in range(int(n/2)):
            if s_clean[i] != s_clean[-1-i]:
                return False

        return True