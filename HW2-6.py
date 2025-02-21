'''
PROCEDURE
MaximumVertexDisjointPaths(G, s, t):
# 建構流網絡
flow_network = ConstructFlowNetwork(G, s, t)

# 使用最大流算法找出最大流量
max_flow = MaxFlow(flow_network, s, t)

# 從最大流量中找出所有的增廣路徑
paths = []
while max_flow > 0:
    path = FindAugmentingPath(flow_network, s, t)
    paths.append(path)
    UpdateResidualGraph(flow_network, path)
    max_flow -= 1

return paths

PROCEDURE
ConstructFlowNetwork(G, s, t):
# 複製原圖 G
flow_network = G.copy()

# 為每個節點 v ∈ V \ {s, t} 創建兩個節點 v_in 和 v_out
for v in V(G) - {s, t}:
    flow_network.add_vertex(v + '_in')
    flow_network.add_vertex(v + '_out')

    # 將原圖中的入邊連接到 v_in, 出邊連接從 v_out
    for u in predecessors(G, v):
        flow_network.add_edge(u, v + '_in')
    for w in successors(G, v):
        flow_network.add_edge(v + '_out', w)

    # 連接 v_in 和 v_out 並設定容量為 1
    flow_network.add_edge(v + '_in', v + '_out', capacity=1)

# 從源點 s 連接到所有 v_in, 從所有 v_out 連接到匯點 t
for v in V(G) - {s, t}:
    flow_network.add_edge(s, v + '_in', capacity=float('inf'))
    flow_network.add_edge(v + '_out', t, capacity=float('inf'))

return flow_network
'''
