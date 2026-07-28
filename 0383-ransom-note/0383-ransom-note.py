class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Har character ki frequency count bana lo
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        
        # Check karo ki magazine me utne ya usse zyada letters hain ya nahi
        for char, count in note_count.items():
            if mag_count[char] < count:
                return False
                
        return True