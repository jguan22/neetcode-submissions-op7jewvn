class Solution:

    def encode(self, strs: List[str]) -> str:
        # use number before each string to indicate the length
        res = []
        for s in strs:
            length = len(s)
            res.append(str(length))
            res.append("#")
            res.append(s)

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i

            # read char until '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            start_index = j + 1
            end_index = start_index + length

            # add the string with this length into list
            res.append(s[start_index:end_index])

            # update index
            i = end_index
        
        return res
