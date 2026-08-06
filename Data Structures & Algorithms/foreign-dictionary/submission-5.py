class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # graph problem: build the graph as letter order and check if there is cycle in the graph
        adj_list = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        n = len(words)
        for i in range(1, n):
            a = words[i-1]
            b = words[i]

            # edge case: b is prefix of a
            if len(a) > len(b) and a.startswith(b):
                return ""
            
            m = min(len(a), len(b))
            for j in range(m):
                if a[j] != b[j]:
                    if b[j] not in adj_list[a[j]]:
                        adj_list[a[j]].add(b[j])
                        indegree[b[j]] += 1
                    break
        
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for nxt in adj_list[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return "".join(order) if len(order) == len(indegree) else ""