import networkx as nx
import matplotlib.pyplot as plt


def showDirectedGraph(graph):
    nodes = graph.get_vertices()
    ng = nx.DiGraph()
    ng.add_nodes_from(nodes)

    for u in nodes:
        for v in graph.get_edges(u):
            ng.add_edge(u, v, weight=graph.weight(u, v))

    # 绘制图形
    pos = nx.kamada_kawai_layout(ng)  # 选择布局算法
    labels = nx.get_edge_attributes(ng, 'weight')  # 边的权值作为标签

    # 绘制结点
    nx.draw_networkx_nodes(ng, pos, node_color='skyblue', node_size=10)

    # 绘制边
    nx.draw_networkx_edges(ng, pos, arrows=True, arrowsize=20, edge_color='gray')

    # 绘制边的权值标签
    nx.draw_networkx_edge_labels(ng, pos, edge_labels=labels)

    # 绘制结点标签
    nx.draw_networkx_labels(ng, pos, font_color='black', font_size=12)

    plt.axis('off')  # 关闭坐标轴

    plt.savefig("directed_graph.jpg")
    plt.show()  # 显示图形


# 求最短路径，使用Dijkstra算法
def calcShortestPath(graph, word1=None, word2=None):
    word1 = input("请输入word1: ")
    word2 = input("请输入word2: ")
    nodes = graph.get_vertices()
    if word1 not in nodes or word2 not in nodes:
        print("不存在的结点！")
        return
    distances = {node: float('inf') for node in graph.get_vertices()}
    precursor = {node: None for node in graph.get_vertices()}
    distances[word1] = 0
    visited = set()
    while word2 not in visited:
        current_node = min((node for node in graph.get_vertices() if node not in visited),
                           key=lambda n: distances[n])
        visited.add(current_node)

        neighbors = graph.get_edges(current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                weight = graph.weight(current_node, neighbor)
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    precursor[neighbor] = current_node

    path = []
    current_node = word2
    while current_node != word1:
        if current_node is None:
            print(f"单词{word1}与{word2}不可达！")
            return
        path.insert(0, current_node)
        current_node = precursor[current_node]

    path.insert(0, word1)
    print(f"单词{word1}与{word2}间的最短距离为{distances[word2]}，路径如下：")
    print("→".join(path))

    # 绘制部分
    nodes = graph.get_vertices()
    ng = nx.DiGraph()
    ng.add_nodes_from(nodes)

    for u in nodes:
        for v in graph.get_edges(u):
            ng.add_edge(u, v, weight=graph.weight(u, v))

    # 绘制图形
    pos = nx.kamada_kawai_layout(ng)  # 选择布局算法
    labels = nx.get_edge_attributes(ng, 'weight')  # 边的权值作为标签
    # 绘制结点
    nx.draw_networkx_nodes(ng, pos, node_color='skyblue', node_size=10)
    # 绘制边
    nx.draw_networkx_edges(ng, pos, arrows=True, arrowsize=20, edge_color='gray')

    path_style = {
        "edge_color": "red",
        "width": 5,
    }

    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(ng, pos, edgelist=path_edges, **path_style)
    # 绘制边的权值标签
    nx.draw_networkx_edge_labels(ng, pos, edge_labels=labels)
    # 绘制结点标签
    nx.draw_networkx_labels(ng, pos, font_color='black', font_size=12)
    plt.axis('off')  # 关闭坐标轴
    plt.savefig("shortest_path.jpg")
    plt.show()  # 显示图形
