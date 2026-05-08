class Solution:
    def decodeString(self, s: str) -> str:
        # use stack
        stack = []
        for c in s:
            if c == ']':
                # pop previous string needed to be repeated
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()

                # pop int in the front
                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                num = int(digits)

                # repeat the string and push back to stack
                stack.append(num * string)
        
            else:
                stack.append(c)
        
        return "".join(stack)