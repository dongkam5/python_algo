#bfs 구현 연습
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}
def stack_def(start_vertex):
    visited=[]
    stack=[start_vertex]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for item in graph[vertex]:
                stack.append(item)
    return visited