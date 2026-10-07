class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # abs(val) = size
        # ast[i] < abs(ast[i+1]) -> ast[i] destroyed
        # ast[i] == abs(ast[i+1]) -> both destroyed
        # neg and neg cant destry or pos and pos (has to be opposite)
        
        stack = []

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
                continue
            skip = False
            while stack:
                if stack[-1] < 0:
                    break
                elif stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast) :
                    stack.pop()
                    skip = True
                    break
                elif stack[-1] > abs(ast):
                    skip = True
                    break
            if ((stack and stack[-1] < 0) or not stack) and not skip:
                stack.append(ast)
                

        return stack