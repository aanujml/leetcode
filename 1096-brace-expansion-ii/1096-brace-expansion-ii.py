class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        n = len(expression)
        
        def parse_factor() -> set[str]:
            if expression[self.i] == '{':
                self.i += 1 
                res = parse_expr()
                self.i += 1
                return res
            else:
              
                start = self.i
                while self.i < n and expression[self.i].isalpha():
                    self.i += 1
                return {expression[start:self.i]}

        def parse_term() -> set[str]:
            res = {""}
           
            while self.i < n and expression[self.i] not in "},":
                factor = parse_factor()
                res = {w1 + w2 for w1 in res for w2 in factor}
            return res

        def parse_expr() -> set[str]:
            res = parse_term()
            while self.i < n and expression[self.i] == ',':
                self.i += 1  
                res |= parse_term() 
            return res

        return sorted(parse_expr())
