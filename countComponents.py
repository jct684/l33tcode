from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #input: number of nodes and an array
        #output: integer
        # n=4, [[1,2],[2,3],[4,5]] ans = 2
        # n=4, [[1,2],[[4,5], [2,3]], [5,1]] ans = 1
        #bfs starting at a node that has not been visited before until all nodes visited, count number of fresh starts
        #time complexity O(V+E)
        #space complexity O(V+E)
        adj_dict = {}
        for edge in edges:
            if edge[0] not in adj_dict:
                adj_dict[edge[0]] = []
            if edge[1] not in adj_dict:
                adj_dict[edge[1]] = []
            adj_dict[edge[0]].append(edge[1])
            adj_dict[edge[1]].append(edge[0])
        visited = set()
        count = 0
        q = deque()
        for node in adj_dict:
            if node not in visited:
                q.append(node)
                count += 1
                while len(q) > 0:
                    curr_node = q.popleft()
                    visited.add(curr_node)
                    list_nodes = adj_dict[curr_node]
                    for connected_node in list_nodes:
                        if connected_node not in visited:
                            q.append(connected_node)
        return count + n-len(visited)