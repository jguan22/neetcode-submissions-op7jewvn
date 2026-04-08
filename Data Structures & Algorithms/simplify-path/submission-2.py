class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []
        for token in tokens:
            if not token or token == ".":
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        
        new_path = '/' + '/'.join(stack)
        return new_path