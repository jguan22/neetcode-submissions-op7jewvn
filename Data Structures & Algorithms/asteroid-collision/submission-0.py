class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # use stack
        stack = []

        for num in asteroids:
            # collision happens: neg incoming to a pos in stack
            while stack and num < 0 and stack[-1] > 0:
                if abs(num) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(num) == stack[-1]:
                    stack.pop()
                    
                num = 0
            
            if num != 0:
                stack.append(num)
        
        return stack