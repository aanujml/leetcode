class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
       return self.convertToTitle((columnNumber - 1) // 26) + chr(65 + (columnNumber - 1) % 26) if columnNumber else "" 