from collections import deque

def bfs(start, graph):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

bfs(1, graph)