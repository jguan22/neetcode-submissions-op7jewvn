class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build a graph
        adj = defaultdict(list)
        indegree = {c: 0 for word in words for c in word}
        n = len(words)
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            min_len = min(len(word1), len(word2))

            # invalid case
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].append(word2[j])
                        indegree[word2[j]] += 1
                    break
                
        # topological sorting
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        # there is a cycle, invalid case
        if len(res) < len(indegree):
            return ""

        return "".join(res)