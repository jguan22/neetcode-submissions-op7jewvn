class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {'}':'{', ']':'[', ')':'('}
        q = []

        for c in s:
            if c in pair_dict:
                if q and q[-1] == pair_dict[c]:
                    q.pop()
                else:
                    return False
            else:
                q.append(c)
        
        return not q