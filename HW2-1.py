class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {v: [] for v in range(self.V)}
        self.edges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges.append((u, v))

    def remove_edge(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)
        if (u, v) in self.edges:
            self.edges.remove((u, v))
        if (v, u) in self.edges:
            self.edges.remove((v, u))

    def dfs(self, start):
        stack = [start]
        visited = set()
        circuit = []

        while stack:
            current = stack[-1]

            if current not in visited and self.graph[current]:
                visited.add(current)
                next_vertex = self.graph[current].pop()
                stack.append(next_vertex)
                circuit.append((current, next_vertex))
            else:
                stack.pop()

        return circuit

    def find_euler_tour(self):
        start_vertex = 0  # Choose any starting vertex
        circuit = self.dfs(start_vertex)

        while len(circuit) != len(self.edges):
            for edge in circuit:
                self.remove_edge(*edge)

            remaining_edges = [edge for edge in self.edges if edge[0] in self.graph and edge[1] in self.graph]
            if remaining_edges:
                start_vertex = remaining_edges[0][0]
                circuit += self.dfs(start_vertex)
            else:
                break

        return circuit

# Example usage
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    euler_tour = g.find_euler_tour()
    print("Euler Tour:", euler_tour)

'''
1.從任意一個節點開始進行深度優先搜尋 (DFS)。
2.當 DFS 發現重複訪問到起始節點時,便找到了一個環路 (cycle)。
3.檢查這個環路是否為 Euler Tour,也就是檢查該環路是否含有圖中所有邊,且只訪問一次每一條邊。
4.如果是 Euler Tour,則完成,輸出該環路即可。
5.如果不是,則移除該環路。移除後,必定有某個節點仍然有未訪問的邊,從該節點重新開始 DFS。
6.重複步驟 2-5,直到找到 Euler Tour 或是所有邊均已訪問完畢。
7.如果在移除所有環路後,剩餘的邊恰好構成一個環路,那麼將其加入最終的 Euler Tour 中。

procedure FindEulerTour(G):
    start_vertex = 任意一個節點
    circuit = DFS(G, start_vertex)

    while circuit is not Euler Tour:
        remove circuit from G
        if there are remaining edges:
            start_vertex = 任意一個有剩餘邊的節點
            circuit = DFS(G, start_vertex)
        else:
            break

    return circuit

procedure DFS(G, start_vertex):
    form a circuit starting from start_vertex
    while there are unexplored edges from circuit:
        current = circuit's last vertex
        if current has unexplored edges:
            explore one of those edges
            add newly explored path to circuit
        else:
            backtrack to previously explored vertex
    return circuit
'''

'''
def hierholzer_algorithm(graph):
    # Check if the graph is Eulerian
    if not is_eulerian(graph):
        return None
    
    # Initialize variables
    current_path = []
    circuit = []
    
    # Start from a vertex with a non-zero degree
    start_vertex = find_start_vertex(graph)
    current_path.append(start_vertex)
    
    while current_path:
        current_vertex = current_path[-1]
        
        if has_unused_edges(current_vertex, graph):
            # Find and traverse an unused edge
            next_vertex = get_next_vertex(current_vertex, graph)
            current_path.append(next_vertex)
            remove_edge(current_vertex, next_vertex, graph)
        else:
            # Backtrack
            circuit.append(current_path.pop())
    
    return circuit

# Helper functions
def is_eulerian(graph):
    # Check if all vertices have even degree (for Eulerian circuit)
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:
            return False
    return True

def find_start_vertex(graph):
    # Find any vertex with a non-zero degree
    for vertex in graph:
        if len(graph[vertex]) > 0:
            return vertex
    return None

def has_unused_edges(vertex, graph):
    return len(graph[vertex]) > 0

def get_next_vertex(vertex, graph):
    return graph[vertex][0]

def remove_edge(u, v, graph):
    graph[u].remove(v)
    graph[v].remove(u)

'''

'''

def find_euler_tour(graph):
    def find_cycle(start_vertex):
        cycle = []
        stack = [start_vertex]
        
        while stack:
            v = stack[-1]
            if graph[v]:
                u = graph[v].pop()
                stack.append(u)
                graph[u].remove(v)
            else:
                cycle.append(stack.pop())
        
        return cycle

    # 假設圖形以鄰接列表的形式提供
    graph_copy = {v: set(neighbors) for v, neighbors in graph.items()}
    start_vertex = next(iter(graph_copy))
    euler_tour = find_cycle(start_vertex)
    
    for v in euler_tour:
        while graph_copy[v]:
            sub_cycle = find_cycle(v)
            euler_tour = euler_tour[:euler_tour.index(v)] + sub_cycle + euler_tour[euler_tour.index(v) + 1:]
    
    return euler_tour

# 範例圖形（鄰接列表表示）
graph = {
    0: {1, 2},
    1: {0, 2},
    2: {0, 1, 3},
    3: {2, 4, 5},
    4: {3, 5},
    5: {3, 4}
}

print(find_euler_tour(graph))

'''