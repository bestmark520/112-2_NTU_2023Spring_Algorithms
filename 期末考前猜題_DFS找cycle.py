import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, id):
        """節點類，表示圖中的一個節點"""
        self.id = id  # 節點的 ID
        self.color = 'WHITE'  # 節點的顏色 ('WHITE': 未訪問, 'GRAY': 訪問中, 'BLACK': 訪問完成)
        self.pi = None  # 節點的前驅節點
        self.d = 0  # 訪問的起始時間戳
        self.f = 0  # 訪問的結束時間戳
        self.adj = []  # 與該節點相連的鄰接節點

def DFS(G):
    """深度優先搜索 (DFS) 主函式，用於遍歷圖並檢測是否存在環"""
    time = 0  # 全局時間戳初始化
    for v in G:
        v.color = 'WHITE'  # 初始化所有節點的顏色為 'WHITE'
        v.pi = None  # 初始化所有節點的前驅節點為 None

    # 繪製初始圖的狀態
    plt.figure(figsize=(8, 6))
    draw_graph(G, "Initial Graph", time)

    for v in G:
        if v.color == 'WHITE':  # 若節點尚未被訪問，則進行深度優先訪問
            time = DFS_Visit(G, v, time)
            if time == -1:  # 若檢測到環，則立即返回
                draw_graph(G, "Cycle Found in Graph", time)
                plt.show()
                return True

    # 若遍歷完成後未檢測到環，繪製結果圖
    draw_graph(G, "No Cycle Found in Graph", time)
    plt.show()
    return False

def DFS_Visit(G, u, time):
    """深度優先搜索的輔助函式，遞迴地訪問節點"""
    u.d = time + 1  # 記錄節點被訪問的起始時間
    time = u.d  # 更新全局時間戳
    u.color = 'GRAY'  # 將節點顏色標記為 'GRAY' (訪問中)
    draw_graph(G, f"Visiting Node {u.id}", time)  # 繪製當前節點訪問狀態

    for v in u.adj:  # 遍歷當前節點的所有鄰接節點
        if v.color == 'WHITE':  # 若鄰接節點尚未被訪問
            v.pi = u  # 將當前節點設為鄰接節點的前驅節點
            time = DFS_Visit(G, v, time)  # 遞迴訪問鄰接節點
            if time == -1:  # 若檢測到環，則立即返回
                return -1
        elif v.color == 'GRAY':  # 若鄰接節點正在被訪問，則檢測到環
            draw_graph(G, f"Cycle Found at Node {v.id}", time)
            plt.show()
            return -1

    u.f = time + 1  # 記錄節點訪問完成的時間戳
    time = u.f  # 更新全局時間戳
    u.color = 'BLACK'  # 將節點顏色標記為 'BLACK' (訪問完成)
    draw_graph(G, f"Finished Visiting Node {u.id}", time)  # 繪製節點完成訪問的狀態
    return time

def draw_graph(G, title, time):
    """繪製圖的當前狀態"""
    plt.clf()  # 清除當前的圖像
    plt.title(title)  # 設定圖像標題
    node_colors = ['white', 'gray', 'black']  # 定義節點顏色對應的顏色名稱
    # 生成節點顏色列表，根據節點的顏色屬性進行映射
    node_colors_list = [node_colors[['WHITE', 'GRAY', 'BLACK'].index(node.color)] for node in G]

    G_nx = nx.Graph()  # 初始化 NetworkX 圖物件
    for node in G:
        G_nx.add_node(node)  # 將節點加入 NetworkX 圖
    for node in G:
        for neighbor in node.adj:  # 將所有邊加入 NetworkX 圖
            G_nx.add_edge(node, neighbor)

    pos = nx.spring_layout(G_nx, seed=42)  # 使用 spring layout 計算節點的座標
    # 為節點添加標籤，包含 ID 和時間戳資訊
    node_labels = {node: f"        {node.id} ({node.d}/{node.f})" for node in G_nx.nodes()}
    # 繪製 NetworkX 圖，包含節點顏色和標籤
    nx.draw(G_nx, pos, node_color=node_colors_list, labels=node_labels, with_labels=True)
    plt.pause(1.5)  # 暫停以便觀察繪製的圖


# 節點創建
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

# 添加邊
a.adj = [b]
b.adj = [c, e]
c.adj = [d]
e.adj = [f]
f.adj = [g]
g.adj = [b]  # 調整這邊可以控制有無cycle

# 圖的表示
G = [a, b, c, d, e, f, g]

# 檢查是否有環
has_cycle = DFS(G)
print("Graph has a cycle: ", has_cycle)

'''

用stack 這個資料結構

DFS(G = (V, E))
    for each v ∈ V  # 對圖中的每個節點v
        v.color = WHITE  # 初始化節點的顏色為白色，表示尚未訪問
        v.π = NIL  # 初始化節點的前驅為空
    time = 0  # 初始化時間計數器

    for each v ∈ V  # 再次遍歷圖中的每個節點v
        if v.color == WHITE  # 如果節點v尚未被訪問
            if DFS-Visit(G, v, time) == true  # 對節點v進行深度優先訪問
                return true  # 找到環，返回true
    return false  # 如果遍歷完所有節點後沒有發現環，返回false

DFS-Visit(G = (V, E), u, time)
    time = time + 1  # 遞增時間計數器
    u.d = time  # 記錄節點u的發現時間
    u.color = GRAY  # 將節點u標記為灰色，表示正在訪問

    for each v ∈ Adj[u]  # 對於每個與u相鄰的節點v
        if v.color == WHITE  # 如果節點v尚未被訪問
            v.π = u  # 設置v的前驅為u
            if DFS-Visit(G, v, time) == true  # 對節點v進行深度優先訪問
                return true  # 找到環，返回true
        elif v.color == GRAY  # 如果發現灰色的節點，表示存在環
            return true  # 找到環，返回true

    time = time + 1  # 遞增時間計數器
    u.f = time  # 記錄節點u的完成時間
    u.color = BLACK  # 將節點u標記為黑色，表示訪問完成

    return false  # 如果沒有發現環，返回false

'''

