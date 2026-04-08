class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                string = ""
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)

                stack.append(int(k) * string)

        return "".join(stack)