#graph is a dictionary with edges represented by key:value pairs where the keys and values are integers
#this is meant to detect and print a cycle in an undirected graph
#time complexity O(n+m)
#space compelxity O(n)

def detect_print_cycle(graph):
    root = 1
    cycle=[]
    DFS(root, graph, cycle)
    if len(cycle) == 0:
        print("No cycle found")
    else:
        return cycle

def DFS(root, graph, cycle, visited={}, parents={}):
    visited[root] = True
    for i in range(len(graph[root])):
        if graph[root][i] is not parents.get(root, False):
            if graph[root][i] in visited:
                cycle.append(root)
                return graph[root][i]
            parents[graph[root][i]] = root
            found = DFS(graph[root][i], graph, cycle, visited, parents)
            if found:
                if found != root:
                    cycle.append(root)
                    return found
                else:
                    cycle.append(root)
                    return cycle
    return ""