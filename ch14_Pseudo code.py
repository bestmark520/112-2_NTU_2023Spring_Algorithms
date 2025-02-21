'''

#ch14_Prim

# r是起點

MST-Prim(G = (V, E, w), r)
1. for each u ∈ V  # 對於圖中的每個節點u
2.     u.key = ∞  # 初始化u的鍵值為無限大
3.     u.π = NIL  # 初始化u的前驅為空
4. r.key = 0  # 將起點r的鍵值設置為0
5. Q = ∅  # 初始化優先隊列Q
6. for each u ∈ V  # 將所有節點加入優先隊列Q
7.     Insert(Q, u)  # 將u插入優先隊列Q

8. while Q ≠ ∅  # 當優先隊列Q不為空時
9.     u = Extract-Min(Q)  # 從Q中取出鍵值最小的節點u
10.    for each v ∈ adj[u]  # 對於每個與u相鄰的節點v
11.        if v ∈ Q and w(u, v) < v.key  # 如果v在Q中且邊(u, v)的權重小於v的鍵值
12.            v.π = u  # 更新v的前驅為u
13.            v.key = w(u, v)  # 更新v的鍵值為邊(u, v)的權重
14.            Decrease-Key(Q, v, w(u, v))  # 調整Q中v的位置，以反映其鍵值的變化
15. return A = {(v.π, v) | v ∈ V \ {r}}  # 返回最小生成樹的邊集合A

# 假設有輔助函數Insert, Extract-Min, Decrease-Key來操作優先隊列Q

#簡介：由起點r出發，每次都選權重最少的邊走，不能連成cycle
#時間複雜度：O(|V|log|V| +|E|)

===

#ch14_Kruskal

MST-Kruskal(G = (V, E, w))
1. A = ∅  # 初始化最小生成樹的邊集合A為空
2. for each v ∈ V  # 對於圖中的每個節點v
3.     Make-Set(v)  # 將每個節點v獨立地設置為一個集合
4. edges = list(E)  # 創建一個用來存儲邊的列表edges，包含圖中的所有邊

5. Sort(edges, key=lambda (u, v): w(u, v))  # 將邊按權重從小到大排序
6. for each edge (u, v) in edges  # 遍歷排序後的邊列表
7.     if Find-Set(u) ≠ Find-Set(v)  # 如果u和v不屬於同一個集合 #所以不會有cycle
8.         A = A ∪ {(u, v)}  # 將邊(u, v)加入最小生成樹的邊集合A
9.         Union(u, v)  # 合併u和v所在的集合
10. return A  # 返回最小生成樹的邊集合A

# 假設有輔助函數Make-Set, Find-Set, Union來操作不相交集合

#簡介：沒有起點，從最少的權重開始選，不能連成cycle
#時間複雜度：O(|E|log|V|)

'''