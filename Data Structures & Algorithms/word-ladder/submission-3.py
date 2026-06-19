class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # sanity check
        if endWord not in wordList:
            return 0

        # convert it to a graph problem, each word is a node
        # find a path from begin to end
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        n = len(beginWord)

        # loop through all words and intermediate O(m * n^2)
        for word in wordList:
            for i in range(n):
                # use intermediate to connect two word nodes
                intermediate = word[:i] + '*' + word[i+1:]

                adj_list[word].append(intermediate)
                adj_list[intermediate].append(word)
        
        # bfs from beginWord
        queue = deque([(beginWord, 1)])
        visited = set()

        # total edges 2*m*n
        while queue:
            curr, step = queue.popleft()

            if curr in visited:
                continue
            visited.add(curr)

            # base case
            if curr == endWord:
                return step
            
            for intermediate in adj_list[curr]:
                for nxt in adj_list[intermediate]:
                    if nxt not in visited:
                        queue.append((nxt, step + 1))

        return 0
