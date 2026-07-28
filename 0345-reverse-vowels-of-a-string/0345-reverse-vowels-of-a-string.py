class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        
        while left < right:
            # Jab tak left par vowel na mile, aage badho
            if s[left] not in vowels:
                left += 1
            # Jab tak right par vowel na mile, peeche aao
            elif s[right] not in vowels:
                right -= 1
            # Dono jagah vowel milte hi swap kar do
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        return "".join(s)