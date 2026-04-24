def dfs(node, graph, visited):
    # 1. stop if already visited
    if node in visited:
        return

    # 2. visit node
    print(node)
    visited.add(node)

    # 3. go deeper
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)

graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

visited = set()
dfs(1, graph, visited)