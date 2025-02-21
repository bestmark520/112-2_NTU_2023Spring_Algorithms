'''

#ch12_BSF

# s是起點
# 初始化
for each u ∈ V - {s}
    u.color = WHITE, u.d = ∞, u.π = NIL  # 將每個節點的顏色設為白色，距離設為無限，前驅設為空
s.color = GRAY, s.d = 0, s.π = NIL  # 將起點s的顏色設為灰色，距離設為0，前驅設為空
Q = ∅ and ENQUEUE(Q,s)  # 初始化空隊列並將起點s加入隊列

# 當隊列不為空時，執行以下操作
while Q ≠ ∅
    u = DEQUEUE(Q)  # 從隊列中取出一個節點u
    for each v ∈ Adj[u]  # 對於每個與u相鄰的節點v
        if v.color == WHITE  # 如果節點v的顏色是白色
            v.color = GRAY, v.d = u.d + 1, v.π = u  # 將v的顏色設為灰色，距離設為u的距離加1，前驅設為u
            ENQUEUE(Q,v)  # 將v加入隊列

    u.color = BLACK  # 將u的顏色設為黑色，表示u已經被完全探索

#簡介：把u拿出來，所有u的下一個都是v，那v的距離就是u+1，v的前一個是u，此時u的周遭都灰色了，所以u變黑色
#時間複雜度：O(|V| +|E|)

===

#ch12_DSF

#初始化
DFS(G = (V, E))
for each v ∈ V  # 對圖中的每個節點v
    v.color = WHITE  # 初始化節點的顏色為白色，表示尚未訪問
    v.π = NIL  # 初始化節點的前驅為空
time = 0  # 初始化時間計數器

#迴圈
for each v ∈ V  # 再次遍歷圖中的每個節點v
    if v.color == WHITE  # 如果節點v尚未被訪問
        DFS-Visit(G, v, time)  # 對節點v進行深度優先訪問

#迴圈的程式
DFS-Visit(G = (V, E), u, time)
time = time + 1  # 遞增時間計數器

u.d = time  # 記錄節點u的發現時間 #起點
u.color = GRAY  # 將節點u標記為灰色，表示正在訪問
for each v ∈ Adj[u]  # 對於每個與u相鄰的節點v
    if v.color == WHITE  # 如果節點v尚未被訪問
        v.π = u  # 設置v的前驅為u
        DFS-Visit(G, v, time)  # 對節點v進行深度優先訪問
time = time + 1  # 遞增時間計數器

u.f = time  # 記錄節點u的完成時間 #終點
u.color = BLACK  # 將節點u標記為黑色，表示訪問完成

#迴圈內再一個跟自己一樣的迴圈，藉此達到走路紀錄time-mark的效果

#簡介：從起點u開始走，紀錄每個點在第幾步走到，直到cycle再走回頭路回起點u
#時間複雜度：O(|V| +|E|)

'''
import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        pos[node.value] = (x, y)
        if node.left:
            graph.add_edge(node.value, node.left.value)
            l = x - 1 / layer
            add_edges(graph, node.left, pos, x=l, y=y-1, layer=layer+1)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            r = x + 1 / layer
            add_edges(graph, node.right, pos, x=r, y=y-1, layer=layer+1)

def plot_tree(root):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)
    nx.draw(graph, pos, with_labels=True, arrows=False, node_size=3000, node_color='skyblue', font_size=16, font_weight='bold')
    plt.show()

# 建立範例樹
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 繪製樹的結構
plot_tree(root)
