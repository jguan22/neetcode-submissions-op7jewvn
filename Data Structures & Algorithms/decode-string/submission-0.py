class Solution:
    def decodeString(self, s: str) -> str:
        # maintain a stack and parse the string
        stack = []

        for c in s:
            # push char into stack until reach any ']'
            if c != ']':
                stack.append(c)
            else:
                # pop char from stack until '['
                substring = ""
                while stack and stack[-1] != '[':
                    # in reversed order
                    substring = stack.pop() + substring
                stack.pop()

                # pop int before '[]'
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # parse string 
                string = int(k) * substring
                stack.append(string)
        
        return "".join(stack)