class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            curr_len = int(s[i:j])
            i = j+1+curr_len
            decoded.append(s[j+1:i])
        return decoded
            

