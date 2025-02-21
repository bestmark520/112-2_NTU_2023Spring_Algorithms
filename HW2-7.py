'''
def ford_fulkerson(graph, source, sink):
    max_flow = 0
    while True:
        # Find a path from source to sink using BFS
        path, path_flow = bfs(graph, source, sink)
        if path_flow == 0:
            break
        # Add path flow to overall flow
        max_flow += path_flow
        # Update capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = path[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
    return max_flow

def bfs(graph, source, sink):
    visited = {source}
    queue = [(source, float('Inf'))]
    parent = {}

    while queue:
        u, flow = queue.pop(0)
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                new_flow = min(flow, graph[u][v])
                if v == sink:
                    return parent, new_flow
                queue.append((v, new_flow))
    return None, 0

===
# 初始化
for each u ∈ V
    for each v ∈ Adj[u]
        capacity[u][v] = initial_capacity[u][v]  # 初始化每條邊的容量

max_flow = 0  # 初始化最大流量為0

# 循環尋找增廣路徑
while True
    for each u ∈ V - {s}
        u.color = WHITE, u.d = ∞, u.π = NIL  # 將每個節點的顏色設為白色，距離設為無限，前驅設為空
    s.color = GRAY, s.d = 0, s.π = NIL  # 將起點s的顏色設為灰色，距離設為0，前驅設為空
    Q = ∅  # 初始化空隊列
    ENQUEUE(Q, s)  # 將起點s加入隊列

    path_found = False  # 記錄是否找到增廣路徑

    # 當隊列不為空時，執行以下操作
    while Q ≠ ∅
        u = DEQUEUE(Q)  # 從隊列中取出一個節點u
        for each v ∈ Adj[u]  # 對於每個與u相鄰的節點v
            if v.color == WHITE and capacity[u][v] - flow[u][v] > 0  # 如果節點v的顏色是白色且有剩餘容量
                v.color = GRAY, v.d = u.d + 1, v.π = u  # 將v的顏色設為灰色，距離設為u的距離加1，前驅設為u
                ENQUEUE(Q, v)  # 將v加入隊列
                if v == t  # 如果找到達終點t的路徑
                    path_found = True
                    break
        if path_found
            break
        u.color = BLACK  # 將u的顏色設為黑色，表示u已經被完全探索

    if not path_found
        break  # 如果沒有找到增廣路徑，退出循環

    # 找到增廣路徑後，計算該路徑上的最小剩餘容量
    path_flow = ∞
    v = t
    while v ≠ s
        u = v.π
        path_flow = min(path_flow, capacity[u][v] - flow[u][v])
        v = u

    # 更新增廣路徑上的流量
    v = t
    while v ≠ s
        u = v.π
        flow[u][v] += path_flow
        flow[v][u] -= path_flow
        v = u

    # 增加總流量
    max_flow += path_flow

# 返回最大流量
return max_flow

時間複雜度為 O(EU)。

'''