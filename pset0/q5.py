class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.visited = [False] * n

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def get_longest_path(self):
        # start from each node and find the longest path
        longest = 0
        for i in range(self.n):
            self.visited = [False] * self.n
            longest = max(longest, self._get_longest_path(i, 0))
        return longest

    def _get_longest_path(self, node, length):
        self.visited[node] = True
        longest = length
        for u, v in self.edges:
            if u == node and not self.visited[v]:
                longest = max(longest, self._get_longest_path(v, length + 1))
        self.visited[node] = False
        return longest