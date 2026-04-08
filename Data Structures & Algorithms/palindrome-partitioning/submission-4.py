class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        combinations = []

        def isPalindrome(substr):
            return substr == substr[::-1]
        
        def dfs(start, combi):
            if start >= n:
                combinations.append(combi[:])
                return
            
            for i in range(start + 1, n + 1):
                if isPalindrome(s[start:i]):
                    combi.append(s[start:i])
                    dfs(i, combi)
                    combi.pop()


        dfs(0, [])
        return combinations