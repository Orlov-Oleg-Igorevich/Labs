import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start, stop = False):
    distances = {v: float('infinity') for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    processed = set()
    parents = {v: None for v in graph}

    while queue:
        current_distance, current_vertex = min(queue, key=lambda x: x[0])
        processed.add(current_vertex)
        queue.remove(min(queue, key=lambda x: x[0]))

        # Обрабатываем только вершину с наименьшим расстоянием
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
                parents[neighbor] = current_vertex

        if stop and all(n in processed for n in graph[stop].keys()):
            return distances[stop], parents

        

    return distances, parents

def PATH (end, parents):
    path = [end]
    parent = parents[end]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 3, 'B': 2}
}

a, b = dijkstra(graph, 'A')
path = PATH('C', b)
path2 = set()

for i in range(len(path)-1):
    path2.add((path[i], path[i+1]))


G = nx.DiGraph()

G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "A", weight=3)
G.add_edge("C", "B", weight=2)
G.add_edge("B", "A", weight=1)
G.add_edge("B", "C", weight=1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) in path2]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) not in path2]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=300)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
