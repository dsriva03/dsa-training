class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):

    if not node:
        return None

    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        
        clone = Node(node.val)
        old_to_new[node] = clone

        for nei in node.neighbors:
            clone.neighbors.append(dfs(nei))
        
        return clone
    
    return dfs(node)
    
