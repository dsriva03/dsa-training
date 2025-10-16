from collections import deque

def bfs(start):
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print("visiting: ", node)

        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
