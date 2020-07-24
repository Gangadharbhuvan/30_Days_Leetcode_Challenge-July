'''
    Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.



'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        paths = [[] for _ in range(N)]
        # Base Case
        paths[-1].append([N-1])
        
        def dfs(node):
            # Check if we already have paths available for the current node
            if not paths[node]:
                for nbr in graph[node]:
                    res = dfs(nbr)
                    # Add current node to each path from neighbour node to target node
                    for r in res:
                        paths[node].append([node] + r)

            return paths[node]
        
        dfs(0)
        return paths[0]