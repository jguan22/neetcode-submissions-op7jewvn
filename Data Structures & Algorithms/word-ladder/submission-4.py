class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # convert it to a graph probelm: use '*' as intermediate nodes
        # edge case
        if endWord not in wordList:
            return 0
        
        # build the graph: O(N * L^2)
        wordList.append(beginWord)
        n = len(beginWord)
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(n):
                intermediate = word[:i] + '.' + word[i+1:]
                adj_list[intermediate].append(word)
            
        # bfs from the beginWord: O(N * L^2)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            curr, dist = queue.popleft()
            if curr == endWord:
                return dist

            for i in range(n):
                intermediate = curr[:i] + '.' + curr[i+1:]
                for nxt in adj_list[intermediate]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, dist + 1))
        
        return 0