
# given a graph (could be unconnected graph) loop over all nodes in the graph with dfs
def dfs(g):
    visited = {}

    for node in g:
        if node not in visited:
            dfs_helper(node, g, visited)
        

def dfs_helper(node, g, visited):
    visited[node] = True
    print(node)
    edges = g[node]
    for edge in edges:
        if edge not in visited:
            dfs_helper(edge, g, visited)
    
    


"""
A -- B
     |
     C

e -- f
"""
g = {
    "A": ["B"], 
    "B": ["A", "C"], 
    "C": ["B"],
    "e": ["f"],
    "f": ["e"]
}

dfs(g)
