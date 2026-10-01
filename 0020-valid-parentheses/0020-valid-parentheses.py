class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Agar stack empty hai ya top element match nahi hota
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # Agar open bracket hai to stack me daal do
                stack.append(char)
                
        return len(stack) == 0