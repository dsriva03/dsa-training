from collections import deque

def ncc_bfs(n, edges):

    #make list
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    seen = set()
    components = 0

    def bfs(start):
        q = deque([start])

        while q:
            node = q.popleft()
            seen.add(node)

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
    
    for node in range(n):
        if node not in seen:
            components += 1
            bfs(node)
    return components

        




        