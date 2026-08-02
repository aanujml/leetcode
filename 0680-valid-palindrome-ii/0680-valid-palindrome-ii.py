class Solution:
    def validPalindrome(self, s: str) -> bool:
        j=len(s)-1
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
    
        for i in range (len(s)//2 + 1):
            if s[i]== s[j]:
                j -=1
            else:
                return isPalindrome(i,j-1) or isPalindrome(i+1,j)
        return True