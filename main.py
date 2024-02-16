class DisjointSet:
def __init__(self, vertices):
self.parent = {v: v for v in vertices}
self.rank = {v: 0 for v in vertices}
def find(self, v):
if self.parent[v] != v:
self.parent[v] = self.find(self.parent[v])
return self.parent[v]
def union(self, v1, v2):
root1 = self.find(v1)
root2 = self.find(v2)
if root1 != root2:
if self.rank[root1] < self.rank[root2]:
self.parent[root1] = root2
elif self.rank[root1] > self.rank[root2]:
self.parent[root2] = root1
else:
self.parent[root1] = root2
self.rank[root2] += 1
def kruskal(graph):
vertices = set()
edges = []
for edge in graph:
vertices.add(edge[0])
vertices.add(edge[1])
edges.append(edge)
vertices = list(vertices)
vertices.sort()
disjoint_set = DisjointSet(vertices)
minimum_spanning_tree = []
# Sorting edges by cost
edges.sort(key=lambda x: x[2]) # Time complexity: O(E log E), where E is the number of edges
for edge in edges:
v1, v2, weight = edge
# Using disjoint set to check if adding the edge creates a cycle
if disjoint_set.find(v1) != disjoint_set.find(v2):
minimum_spanning_tree.append(edge)
disjoint_set.union(v1, v2)
# Overall time complexity: O(E log E)
return minimum_spanning_tree
# Example usage:
# Graph represented as a list of tuples (vertex1, vertex2, cost)
graph = [
('A', 'B', 6),
('A', 'D', 6),
('B', 'C', 1),
('A', 'C', 6),
('C', 'D', 2),
('B', 'E', 2),
('C', 'E', 7),
('C', 'G', 2),
('E', 'F', 4),
('F', 'G', 11),
('D', 'J', 18),
('G', 'I', 2),
('G', 'H', 22),
('F', 'H', 10),
('H', 'I', 12),
('I', 'J', 1),
('J', 'L', 8),
('L', 'K', 3),
('H', 'K', 25),
('I', 'K', 16),
]
# Calculate time complexity
import time
start_time = time.time()
min_spanning_tree = kruskal(graph)
end_time = time.time()
running_time = end_time - start_time
# Print time complexity and minimum spanning tree
print(f"Time Complexity: O(E log E)")
print("Minimum Spanning Tree:", min_spanning_tree)
print(f"Running Time: {running_time} seconds")