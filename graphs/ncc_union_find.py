def ncc_union_find(n, edges):
    parent = []

    for i in range(n):
        parent.append(i)

    comp = n
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        
        return parent[node]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            parent[rootB] = rootA
            return True
        
        return False
    
    for a, b in edges:
        if union(a, b):
            comp -= 1
        
    return comp

