def graph_valid_tree(n, edges):
    num_of_edges = len(edges)
    if num_of_edges != n - 1:
        return False
    
    graph = {}

    for i in range(n):
        graph[i] = []

    for a, b in edges:
        graph[b].append(a)
        graph[a].append(b)

    seen = set()

    def dfs(node, parent):
        seen.add(node)
        for nei in graph[node]:
            if nei == parent:
                continue
            if nei in seen:
                return False
            
            if not dfs(nei, node):
                return False
            
        return True
    
    return dfs(0, -1) and len(seen) == n



