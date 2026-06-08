graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Node: ")
    neighbors = input("Neighbors (space separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:")
dfs(start)
