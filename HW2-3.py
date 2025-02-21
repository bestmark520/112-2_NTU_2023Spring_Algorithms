'''
PROCEDURE ShortestPath(G, s, t, δ)
    // 初始化距離和前驅節點
    FOR each v in V(G)
        dist[v] = INFINITY
        prev[v] = NULL
    dist[s] = 0

    // 使用邊鬆弛(Edge Relaxation)來更新最短路徑估計值
    FOR i = 1 to δ
        FOR each edge (u, v) in E(G)
            IF dist[u] + w(u, v) < dist[v]
                dist[v] = dist[u] + w(u, v)
                prev[v] = u

    // 檢查是否存在負權重環路
    FOR each edge (u, v) in E(G)
        IF dist[u] + w(u, v) < dist[v]
            RETURN "Graph contains negative weight cycle"

    // 重建最短路徑
    S = []
    u = t
    WHILE u is not NULL
        S.INSERT(u, 0)
        u = prev[u]
    RETURN (dist[t], S.reverse())
END PROCEDURE

時間複雜度是 O(δ⋅∣E∣)

講義中距離是v.d 前一個是v.pi
'''

'''
PROCEDURE ShortestPath(G, s, t, δ)
    // 初始化距離和前驅節點
    FOR each v in V(G)
        d.v = INFINITY
        π.v = NULL
        d.s = 0

    // 使用邊鬆弛(Edge Relaxation)來更新最短路徑估計值
    FOR i = 1 to δ
        FOR each edge (u, v) in E(G)
            IF d.u + w(u, v) < d.v
                d.v = d.u + w(u, v)
                π.v = u

    // 檢查是否存在負權重環路
    FOR each edge (u, v) in E(G)
        IF d.u + w(u, v) < d.v
            RETURN "Graph contains negative weight cycle"

    // 重建最短路徑
    S = []
    u = t
    WHILE u is not NULL
        S.INSERT(u, 0)
        u = π.u
    RETURN (d.t, S.reverse())
END PROCEDURE

時間複雜度是 O(δ⋅∣E∣)
'''