#DFS Algorithm
#Traversal means visiting all the nodes of a graph. Depth first traversal or Depth first Search is a recursive algorithm for searching all the vertices of a graph or tree data structure. In this article, you will learn with the help of examples the DFS algorithm, DFS pseudocode, and the code of the depth first search algorithm with Python program.
#DFS pseudocode

#DFS(G, u)
#    u.visited = true
#    for each v ∈ G.Adj[u]
#        if v.visited == false
#            DFS(G,v)
     
#init() {
#    For each u ∈ G
#        u.visited = false
#    For each u ∈ G
#      DFS(G, u)
#}


#DFS Algorithm


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
