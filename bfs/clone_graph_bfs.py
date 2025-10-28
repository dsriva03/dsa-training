from collections import deque

def clone_graph_bfs(node):
    if not node:
        return None

    #make the first clone and start the queue
    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        cur = queue.popleft()

        #loop thru neighbors
        for nei in cur.neighbors:
            if nei not in old_to_new:
                old_to_new[nei] = Node(nei.val)
                queue.append(nei)
            old_to_new[cur].neighbors.append(old_to_new[nei])
    
    return old_to_new[node]


