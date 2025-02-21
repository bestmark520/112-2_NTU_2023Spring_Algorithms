'''
PROCEDURE ComputeAllPairDistances(G, t)
    n = |V(G)|
    dist = AllocateMatrix(n, n) // 初始化距離矩陣
    FOR i = 1 to n
        FOR j = 1 to n
            IF i == j
                dist[i][j] = 0
            ELSE
                dist[i][j] = INFINITY

    FOR l = 1 to t
        FOR u = 1 to n
            FOR v = 1 to n
                FOR w = 1 to l
                    IF dist[u][w] + w(w, v) < dist[u][v]
                        dist[u][v] = dist[u][w] + w(w, v)

    RETURN dist
END PROCEDURE
'''