'''

#ch15_two operation

# 初始化操作
Initialization(G, s)
1. for each v ∈ V  # 對於圖中的每個節點v
2.     v.d = ∞  # 初始化v的距離為無限大
3.     v.π = NIL  # 初始化v的前驅節點為空
4. s.d = 0  # 將起點s的距離設置為0

# relax = 更新，不斷更新最短距離操作
Relax(u, v, w)
1. if v.d > u.d + w(u, v)  # 如果從u經由邊(u, v)到v的距離小於v當前的距離
2.     v.d = u.d + w(u, v)  # 更新v的距離為從u到v的距離
3.     v.π = u  # 更新v的前驅節點為u

===

#ch15_Bellman-Ford

Bellman-Ford(G = (V, E, w), s)
1. Initialization(G, s)  # 初始化圖G中的節點，將起點s的距離設置為0，其他節點的距離設置為無限大

2. for i = 1 to |V| - 1  # 重複|V|-1次
3.     for each edge (u, v) ∈ E  # 對於圖G中的每條邊(u, v)
4.         Relax(u, v, w)  # 執行鬆弛操作，更新v的距離和前驅節點

5. for each edge (u, v) ∈ E  # 再次遍歷所有邊，檢查是否存在負權重環
6.     if v.d > u.d + w(u, v)  # 如果可以找到一條更短的路徑，則存在負權重環
7.         return False  # 返回False，表示圖中存在負權重環

8. return True  # 返回True，表示沒有找到負權重環，所有最短路徑已計算完成

# 假設 Initialization 和 Relax 函數已經定義

#比較：ch14最小生成樹不是起點到某點的最短距離，ch15的Single-Source是起點到所有點的最短距離
#簡介：由起點s出發，不斷relax更新最短距離，可以處理負數邊
#時間複雜度：O(|V||E|)

===

#ch15_有向無環圖(Directed Acyclic Graph, DAG)的最短路徑算法

DAG-Shortest-Path(G, s)
1. Topologically sort the vertices of G.V  # 對圖G中的節點進行拓撲排序
2. Initialization(G, s)  # 初始化操作，設置起點s的距離為0，其他節點的距離為無限大

3. for each vertex u taken from the topological sorted order  # 根據拓撲排序順序遍歷每個節點u
4.     for each vertex v in Adj[u]  # 對於節點u的每個鄰接節點v
5.         Relax(u, v, w)  # 執行鬆弛操作，更新節點v的距離和前驅節點，如果從u到v的距離更短

# 假設 Initialization 和 Relax 函數已經定義

#簡介：沒有cycle，線有方向，不斷更新topologically sort的最短距離
#時間複雜度：O(|V|+|E|)

===

#ch15_Dijkstra

Dijkstra(G = (V, E, w), s)
1. Initialization(G, s)  # 初始化操作，設置起點s的距離為0，其他節點的距離為無限大

2. S = ∅  # S集合，存放已確定最短路徑的節點
3. Q = V  # Q優先隊列，存放未確定最短路徑的節點

4. Insert(Q, s)  # 將起點s插入優先隊列Q

5. while Q ≠ ∅  # 當優先隊列Q不為空時
6.     u = Extract-Min(Q)  # 從Q中取出鍵值最小的節點u
7.     S = S ∪ {u}  # 將節點u加入已確定最短路徑的集合S

8.     for each v in adj[u]  # 對於節點u的每個鄰接節點v
9.         Relax(u, v, w)  # 執行鬆弛操作，更新節點v的距離和前驅節點，如果從u到v的距離更短

# 假設 Initialization, Insert, Extract-Min, 和 Relax 函數已經定義

#簡介：1.可以是有向圖或無向圖 2.不能有負數權重邊 3.速度是最快的
#時間複雜度：O(|V|log|V| +|E|)

'''