class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # sanity check
        if endWord not in wordList:
            return 0

        # build graph with intermediates where '*' represents trasnformation
        wordList.append(beginWord)
        n = len(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(n):
                intermediate = word[:i] + '*' + word[i+1:]
                adj[word].append(intermediate)
                adj[intermediate].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            curr, step = queue.popleft()
            if curr == endWord:
                return step
            
            if curr in visited:
                continue
            visited.add(curr)

            for i in range(n):
                intermediate = curr[:i] + '*' + curr[i+1:]
                for nxt in adj[intermediate]:
                    if nxt not in visited:
                        queue.append((nxt, step + 1))
        
        return 0