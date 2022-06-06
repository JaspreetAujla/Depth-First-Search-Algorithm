def dfs(graph, s, v=None):
    if v is None:
        v = set()
    v.add(s)

    print(s)

    for next in graph[s] - v:
        dfs(graph, next, v)
    return v


graph = {'0': set(['0', '1']),
         '1': set(['2', '3', '4']),
         '2': set(['0']),
         '3': set(['2']),
         '4': set(['3', '4']),
         '5': set(['4', '5'])}

dfs(graph, '5')
