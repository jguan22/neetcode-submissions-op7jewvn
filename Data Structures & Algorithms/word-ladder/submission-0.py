class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # words can change one letter at a time (hit to *ht, h*t, hi*)
        if endWord not in wordList:
            return 0
            
        # use a dict to track all possible change to original word
        word_map = defaultdict(list)
        n = len(beginWord)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(n):
                marked_word = word[:i] + '*' + word[i+1:]
                word_map[word].append(marked_word)
                word_map[marked_word].append(word)
        
        # now that all words are connected, we can use dict as a graph to do bfs
        queue = deque()
        queue.append(beginWord)
        visited = set()
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                word = queue.popleft()
                visited.add(word)

                if word == endWord:
                    return count

                for mid_word in word_map[word]:
                    for transform in word_map[mid_word]:
                        if transform in visited:
                            continue
                        
                        queue.append(transform)
            
        return 0