class Solution:
    def isValid(self, s: str) -> bool:
        br = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for el in s:
            if el in br.values():
                stack.append(el)
            elif stack and stack[-1] == br[el]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0
        