# we can solve graph problems using `3` ways
## DFS {iterative approach using stack, recursive approach}
## BFS { using queue}
class Graph():
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end= ' ')
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                for neighbour in reversed(self.graph[node]):
                    if neighbour not in visited:
                        stack.append(neighbour)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node, end=' ')  # Visit the node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            
if __name__ == "__main__":
    g = Graph()

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("DFS (Recursive):", end='\n')
    g.dfs_recursive(0)  # Output: 0 1 2 3 4
    print("\nDFS (iterative):", end='\n')
    g.dfs_iterative(0)
    print("\nBFS :", end='\n')
    g.bfs(0)