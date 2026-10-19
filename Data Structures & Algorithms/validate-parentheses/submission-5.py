class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack: return False
                openB = stack.pop()

                if openB == '(' and char != ')' or openB == '{' and char != '}' or openB == '[' and char != ']':
                    return False
        return True if not stack else False