'''
Ford-Fulkerson(G = (V,E, c, s, t))

#簡介：把進去跟剩餘的流量分成兩條不同方向的箭頭，
從箭頭中填補滿其中一條從起點到終點的路徑，
最後再把不同方向的箭頭回歸為一開始的形式
#時間複雜度：O(|E| · |f⇤|)

1. for each edge (u, v) ∈ E # 對於每條邊 (u, v) 屬於 E
2. (u, v).f = 0 # 初始化每條邊的流量為 0
3. while there exists a path P from s to t in Gf # 當殘餘圖 Gf 中存在從 s 到 t 的增廣路徑 P 時
4. cf (P) = min{cf (u, v) | (u, v) ∈ P} # 計算增廣路徑 P 中每條邊的殘餘容量，取其中的最小值，作為 P 的殘餘容量 cf (P)
5. for edge (u, v) ∈ P # 對於增廣路徑 P 中的每條邊 (u, v)
6. if (u, v) ∈ E # 如果 (u, v) 是原圖 G 中的一條邊
7. (u, v).f = (u, v).f + cf (P) # 增加這條邊的流量 cf (P)
8. else # 如果 (u, v) 不是原圖 G 中的一條邊 (即 (u, v) 是反向邊)
9. (u, v).f = (u, v).f − cf (P) # 減少這條邊的流量 cf (P)
10. return f # 返回最終的流量 f

===
Minimum Cut
#簡介：直接在路徑上切一刀，
c(S,T)只考慮左邊到右邊，
f(S,T)考慮右邊到左邊，f(S,T)必定<= c(S,T)，
當f(S,T)=c(S,T)成立時是最佳解

#時間複雜度：O(|V | + |E|)

===

Bipartite Matching
#簡介：找最大共用頂點的邊，點頂不能重複
#時間複雜度：

'''