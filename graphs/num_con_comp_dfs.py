def ncc(n, edges):
    #make adjacency list
    graph = {}

    for i in range(n):
        graph[i] = []
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    seen = set()

    #naruto dfs 
    def dfs(node):
        if node not in seen:
            seen.add(node)
        
        for nei in graph[node]:
            if nei not in seen:
                dfs(nei)
    components = 0
    #hokage outer 
    for node in range(n):
        if node not in seen:
            components += 1
            dfs(node)

    return components
