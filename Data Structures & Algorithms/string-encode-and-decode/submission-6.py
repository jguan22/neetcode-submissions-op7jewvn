class Solution:

    def encode(self, strs: List[str]) -> str:
        # use len(s) and a special char to determine a string
        output = []
        
        # O(m), where m is the total num of chars
        for s in strs:
            m = len(s)
            output.append(str(m))
            output.append('#')
            output.append(s)
        
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        str_list = []
        m = len(s)
        i = 0

        # O(m), index increments one way
        while i < m:
            # read the len and special char, then string
            j = i
            while s[j] != '#':
                j += 1
            
            str_len = int(s[i:j])
            i = j + 1 + str_len
            str_list.append(s[j+1:i])
        
        return str_list    
