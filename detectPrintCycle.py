#graph is a dictionary with edges represented by key:value pairs where the keys and values are integers
#this is meant to detect and print a cycle in an undirected graph
#time complexity O(n+m)
#space compelxity O(n)

def detect_print_cycle(graph):
    root = 1
    cycle_membership={}
    DFS(root, graph, cycle_membership)
    cycle = [key for key, value in cycle_membership.items() if value == 1]
    if len(cycle) == 0:
        print("No cycle found")
    else:
        return cycle

def DFS(root, graph, cycle_membership, visited={}, parents={}):
    visited[root] = True
    for i in range(len(graph[root])):
        if graph[root][i] is not parents.get(root, False) and cycle_membership.get("found", True):
            if graph[root][i] in visited:
                cycle_membership[graph[root][i]] = 1
                cycle_membership["found"] = False
                current = root
                while current != graph[root][i]:
                    cycle_membership[current] = 1
                    current = parents[current]
                return
            else:
                parents[graph[root][i]] = root
                DFS(graph[root][i], graph, cycle_membership, visited, parents)

