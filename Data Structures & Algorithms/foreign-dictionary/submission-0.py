class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build the graph
        # use zip() to compare words
        adj_list = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj_list}

        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                # check the first different letter
                if a != b:
                    # create an edge from a to b
                    if b not in adj_list[a]:
                        adj_list[a].add(b)
                        indegree[b] += 1
                    break
            
            # edge case: all letters are same but second is the prefix of first
            else:
                if len(first) > len(second):
                    return ""

        # use indegree to determine if there is any cycle
        queue = deque()
        for node in adj_list:
            if indegree[node] == 0:
                queue.append(node)

        count = 0
        ans = ""
        while queue:
            node = queue.popleft()
            ans += node
            count += 1
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return ans if count == len(adj_list) else ""