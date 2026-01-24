# Python program for the Union-Find algorithm to detect cycles in an undirected graph
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Rank is used to keep the tree flat

    def find(self, x):
        # Path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of the sets x and y belong to
        rootX = self.find(x)
        rootY = self.find(y)

        # Union by rank optimization
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # List to store graph edges

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def has_cycle(self):
        # Initialize Union-Find
        uf = UnionFind(self.V)

        # Check for cycles
        for u, v in self.edges:
            if uf.find(u) == uf.find(v):
                return True  # Cycle found
            uf.union(u, v)
        return False  # No cycles


# Create a graph and add edges
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

# Check if the graph contains a cycle
if g.has_cycle():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
