'''
DP-MM (Matrix Multiply)

#簡介：先只能用1個邊，再只能用2個邊，接著開放可以用3個邊
#算APSP時間複雜度：|V|^3 log(|V|)

Fast-MM-APSP(W, n)
for 1 ≤ i ≤ j ≤ n, I(1)ij = wij   // 初始化 I(1) 為輸入的權重矩陣 W
r = 1   // 令 r 初值為 1

while r ≤ log2 n   // 當 r 小於等於 log2 n 時，重複以下步驟
    for i = 1 to n   // 對於每一個起點 i
        for j = 1 to n   // 對於每一個終點 j
            I(2r)ij = ∞   // 初始化 I(2r)ij 為無窮大
        for k = 1 to n   // 對於每一個中間節點 k
            if I(r)ik + I(r)kj < I(2r)ij   // 若經由 k 的路徑比直接路徑更短
                I(2r)ij = I(r)ik + I(r)kj   // 則以經由 k 的路徑更新 I(2r)ij

r = r * 2   // 令 r 加倍，進入下一輪迭代
return D = {I(r)ij} and Π = {π(r)ij}   // 返回最終的距離矩陣 D 和前溯矩陣 Π

===

DP-Floy-Warshall

#簡介：先只能經過點[1]，再只能經過點[1, 2]，接著開放經過點[1, 2, 3]
#時間複雜度：O(n^3)

Floyd-Warshall(W, n)
D(0) = W and Π(0) = {π(0)ij}         // 如前所述,初始化D(0)為權重矩陣W,Π(0)為直接前溯矩陣
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            if d(k-1)ij ≤ d(k-1)ik + d(k-1)kj    // 若經由k點的路徑不比原路徑更短
                d(k)ij = d(k-1)ij               // 則d(k)ij不變
                π(k)ij = π(k-1)ij              // π(k)ij也不變
            else                                // 否則
                d(k)ij = d(k-1)ik + d(k-1)kj    // 更新d(k)ij為經由k點的更短路徑長度
                π(k)ij = π(k-1)kj              // 更新π(k)ij為k點的前溯點

===

30.Johnson's

#簡介：有負數的邊，建立一個s給h值，用起點+原本邊-終點 = 新的邊長，如此原本的最短邊，還會是最短邊
#時間複雜度：O(|V|^2log|V| + |V||E|)

創建G' = (V', E', w')從G = (V, E, w)通過添加一個源點s
#時間複雜度為O(|V| + |E|)
#建立一個新的加權圖G'，其中包含原始圖G的所有節點和邊，
同時添加一個新的源點s，並將s連接到所有其他節點，邊權重為0
V' = V ∪ {s}和E' = E ∪ {(s, v) | v ∈ V}
∀v ∈ V, w'(s, v) = 0且∀(u, v) ∈ E, w'(u, v) = w(u, v)

對G'應用Bellman-Ford算法來計算h，使得∀v ∈ V
#時間複雜度為O(|V||E|)
#使用Bellman-Ford算法在新圖G'上計算從源點s到每個節點v的最短路徑值h(v)，
如果圖中存在負權重循環，則返回false
h(v) = δ'(s, v)。(如果Bellman-Ford返回false，則返回false)

#對於原始圖G的每個節點v，以v為源點運行Dijkstra算法，重新賦予每條邊(u, v)的權重為w(u, v) + h(u) - h(v)
#時間複雜度為O(|V|(|V|log|V| + |E|)) = O(|V|^2log|V| + |V||E|)
從而獲得新的最短路徑
∀v ∈ V, 對G = (V, E, w)應用Dijkstra算法，以v為源點
- ∀(u, v) ∈ E, w(u, v) = w(u, v) + h(u) - h(v)

'''