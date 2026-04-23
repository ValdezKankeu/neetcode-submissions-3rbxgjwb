class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""
        

        for i in range(len(s)):
            if s[i].isalnum():
                newString += s[i].lower()
        
        l,r = 0, len(newString)-1
        
        while l < r:
            if newString[l] != newString[r]:
                return False
            r -= 1
            l += 1
        
        return True
        