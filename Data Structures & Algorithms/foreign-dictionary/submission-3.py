class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # convert to a graph probelm: look for the topical order
        # loop through the word list to build the graph
        adj_list = defaultdict(list)
        indegree = {c: 0 for word in words for c in word}   # O(C) where C is all letters in list
        n = len(words)
        word1 = words[0]
        # worst case: loop through every words O(C)
        for i in range(1, n):   
            word2 = words[i]
            w1, w2 = len(word1), len(word2)
            
            # edge case: word2 is prefix of word1, wrong order
            if w1 > w2 and word1.startswith(word2):
                return ""

            # scan both words to find the first different char
            for j in range(min(w1, w2)):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].append(word2[j])
                        indegree[word2[j]] += 1
                    break
            
            word1 = word2
        
        # topological sorting: O(V + E), where V is unique char and E is edges
        queue = deque([c for c in indegree if indegree[c] == 0])
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for nxt in adj_list[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        # check if there is cycle in the graph
        if len(ans) != len(indegree):
            return ""
        
        return "".join(ans)
