graph_list = {1: set([2, 5, 9]),
              2: set([3]),
              3: set([4]),
              4: set([]),
              5: set([6, 8]),
              6: set([7]),
              7: set([]),
              8: set([]),
              9: set([10]),
              10: set([])}
root_node = 1

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if graph[n] - set(visited):
                stack += graph[n] - set(visited)
            else:
                print(n)
    return visited

print(DFS_with_adj_list(graph_list, root_node))