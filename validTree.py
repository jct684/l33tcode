class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #input: integer number of nodes, list of edges
        #output: T/F if valid tree
        #n=4 edges = [[0, 1], [1, 2], [0, 3]]
        #n=3 edges = [[0,1], [1,2], [0,2]]
        #n=1
        #time complexity O(V+E)
        #space complexity O(V+E)
        graph = [[] for _ in range(n)]
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for node2 in graph[node]:
                if node2 != prev:
                    if not dfs(node2, node):
                        return False
            return True
        return dfs(0, None) and len(visited) == n