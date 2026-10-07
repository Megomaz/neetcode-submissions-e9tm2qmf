class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # abs(val) = size
        # ast[i] < abs(ast[i+1]) -> ast[i] destroyed
        # ast[i] == abs(ast[i+1]) -> both destroyed
        # neg and neg cant destry or pos and pos (has to be opposite)
        
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast

                if diff > 0:
                    ast = 0
                    break
                elif diff < 0:
                    stack.pop()
                else:
                    ast = 0
                    stack.pop()
                    break
            if ast:
                stack.append(ast)
                

        return stack