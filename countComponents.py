class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #input: number of nodes and an array
        #output: integer
        # n=4, [[1,2],[2,3],[4,5]] ans = 2
        # n=4, [[1,2],[[4,5], [2,3]], [5,1]] ans = 1
        #time complexity O(V+E)
        #space complexity O(V)
        parents = [i for i in range(n)]
        size = [1] * n
        
        def find(n1):
            res = n1
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res
        
        def combine(n2, n3):
            p1, p2 = find(n2), find(n3)
            if p1 == p2:
                return 0
            if size[n2] > size[n1]:
                parents[p2] = p1
                size[n2] += size[n3]
            else:
                parents[p1] = p2
                size[n3] += size[n2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= combine(n1,n2)
        return res