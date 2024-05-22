from textgraph import Graph
import re
import tkinter as tk
from tkinter import filedialog
from show import showDirectedGraph, calcShortestPath, randomWalk

def process_text():
    graph = Graph()
    #用户可视化交互
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    print('输入的文本文件：\n    ', ' '.join(words))
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if word1 != word2:
            graph.add_vertex(word1)
            graph.add_vertex(word2)
            graph.add_edge(word1, word2)

    return graph

# def find_bridge_words(graph):
#
#     word1 = input("请输入word1: ")
#     word2 = input("请输入word2: ")
#
#     if word1 not in graph.graph and word2 not in graph.graph:
#         print("No word1 '{}' and word2 '{}' in the graph!".format(word1, word2))
#     elif word1 not in graph.graph:
#         print("No word1 '{}' in the graph!".format(word1))
#     elif word2 not in graph.graph:
#         print("No word2 '{}' in the graph!".format(word2))
#
#     bridge_words = []
#     for vertex in graph.graph[word1]:
#         if vertex in graph.graph and word2 in graph.graph[vertex]:
#             bridge_words.append(vertex)qse:
#         bridge_words_str = ", ".join(bridge_words)
#         return "The bridge words from {} to {} are: {}.".format(word1, word2, bridge_words_str)


# 示例用法
processed_graph = process_text()

# 输出有向图的节点和边
# for vertex, edges in processed_graph.graph.items():
#     print(vertex, "->", edges)
showDirectedGraph(processed_graph)

calcShortestPath(processed_graph, 'to', 'and')

randomWalk(processed_graph)

# result = find_bridge_words(processed_graph)