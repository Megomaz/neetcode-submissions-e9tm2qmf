class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for num in tokens:
            if num in ['+','-','*','/']:
                r = stack.pop()
                l = stack.pop()

                if num == '+':
                    stack.append((l+r))
                elif num == '-':
                    stack.append((l-r))
                elif num == '*':
                    stack.append((l*r))
                else:
                    stack.append(int(l/r))
            else:
                stack.append(int(num))
            
        return stack[0]


        