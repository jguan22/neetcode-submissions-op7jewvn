class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {c: i for i, c in enumerate(order)}
        
        def compareWord(s1, s2):
            j = 0
            while j < len(s1) and j < len(s2):
                if orderMap[s1[j]] < orderMap[s2[j]]:
                    return True
                elif orderMap[s1[j]] > orderMap[s2[j]]:
                    return False
                j += 1
            
            # if prefix is the same, s1 must be shorter to be valid
            return len(s1) <= len(s2)
        
        for l in range(1, len(words)):
            if not compareWord(words[l-1], words[l]):
                return False
        return True