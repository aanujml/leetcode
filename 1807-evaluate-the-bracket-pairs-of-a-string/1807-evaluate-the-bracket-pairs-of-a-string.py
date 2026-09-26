class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        result = []
        curr_key = []
        in_bracket = False

        for char in s:
            if char == '(':
                in_bracket = True
                curr_key = []
            elif char == ')':
                in_bracket = False
                key_str = "".join(curr_key)
                result.append(lookup.get(key_str, '?'))
            elif in_bracket:
                curr_key.append(char)
            else:
                result.append(char)

        return "".join(result)