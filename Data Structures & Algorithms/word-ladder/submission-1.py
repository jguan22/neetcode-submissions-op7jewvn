class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build the bridge between each words using * to represent char replacement
        adj = defaultdict(list)
        wordList.append(beginWord)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i+1:]
                adj[intermediate].append(word)
        
        # bfs
        queue = deque([beginWord])
        visited = {beginWord}
        step = 0
        while queue:
            n = len(queue)
            step += 1
            for _ in range(n):
                word = queue.popleft()
                for i in range(L):
                    intermediate = word[:i] + '*' + word[i+1:]
                    for nei in adj[intermediate]:
                        if nei == endWord:
                            return step + 1
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
        return 0