from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #time complexity O(V+E)
        #space complexity O(V+E)
        adj_dict = {}
        count_dict = {}
        for entry in prerequisites:
            if(entry[0] not in adj_dict):
                adj_dict[entry[0]] = []
                count_dict[entry[0]] = 0
            if(entry[1] not in adj_dict):
                adj_dict[entry[1]] = []
                count_dict[entry[1]] = 0
            new_edge = adj_dict[entry[1]]
            new_edge.append(entry[0])
            adj_dict[entry[1]] = new_edge
            count_dict[entry[0]] += 1
        
        def cycle_detected():
            queue = deque()
            for node, count in count_dict.items():
                if count == 0:
                    queue.append(node)
            while(len(queue) > 0):
                node = queue.popleft()
                count_dict.pop(node)
                for edge in adj_dict[node]:
                    count_dict[edge] -= 1
                    if count_dict[edge] == 0:
                        queue.append(edge)
            if len(count_dict) > 0:
                return False
            return True
        
        return cycle_detected()