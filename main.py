from graph import Graph
import re
import tkinter as tk
from tkinter import filedialog
from show import showDirectedGraph, calcShortestPath
import random
def process_text():
    graph = Graph()
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

def queryBridgeWords(graph, word1='.', word2='.', flag=0):

    if flag == 0:
        word1 = input("请输入word1: ")
        word2 = input("请输入word2: ")
        if word1 not in graph.graph and word2 not in graph.graph:
            print("No word1 '{}' and word2 '{}' in the graph!".format(word1, word2))
            return
        elif word1 not in graph.graph:
            print("No word1 '{}' in the graph!".format(word1))
            return
        elif word2 not in graph.graph:
            print("No word2 '{}' in the graph!".format(word2))
            return

        bridge_words = []
        for vertex in graph.graph[word1]:
            if vertex in graph.graph and word2 in graph.graph[vertex]:
                bridge_words.append(vertex)

        if not bridge_words:
            print("No bridge words from {} to {}!".format(word1, word2))
        else:
            bridge_words_str = ", ".join(bridge_words)
            print("The bridge words from {} to {} are: {}.".format(word1, word2, bridge_words_str))

    if flag == 1:
        if word1 not in graph.graph or word2 not in graph.graph:
            return []
        bridge_words = []
        for vertex in graph.graph[word1]:
            if vertex in graph.graph and word2 in graph.graph[vertex]:
                bridge_words.append(vertex)
        return bridge_words

def generateNewText(graph):
    input_text = input("请输入新文本: ")
    words = input_text.split()
    new_text = []
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        new_text.append(word1)
        bridge_words = queryBridgeWords(graph, word1, word2, flag=1)
        if len(bridge_words) > 0:
            bridge_word = random.choice(bridge_words)
            new_text.append(bridge_word)
    new_text.append(words[-1])
    output_text = ' '.join(new_text)
    print(output_text)

def randomWalk(graph):
    running = True

    with open('./random_walk.txt', 'w') as f:
        nodes = graph.get_vertices()
        walked = {node: [] for node in nodes}
        start = random.choice(nodes)
        print(f"开始随机游走，起点为{start}...")
        print(start, end='')
        f.write(start)
        current = start
        while running:
            neighbors = graph.get_edges(current)
            if len(neighbors) == 0:
                print(f"\n结点{current}无出边，游走结束。")
                break
            nextnode = random.choice(neighbors)
            if nextnode in walked[current]:
                print(f"\n边{current}→{nextnode}重复，游走结束。")
                break
            else:
                walked[current].append(nextnode)
                print(f" {nextnode}", end='')
                f.write(f" {nextnode}")
                current = nextnode

        if not running:
            print("结束游走。")

def main():
    processed_graph = None
    while True:
        print("请选择要执行的操作:")
        print("1. 处理文本")
        print("2. 显示有向图")
        print("3. 查找桥接词")
        print("4. 插入桥接词")
        print("5. 计算最短路径")
        print("6. 随机游走")
        print("7. 退出")
        choice = input("请输入选项: ")

        if choice == "1":
            processed_graph = process_text()
        elif choice == "2":
            if processed_graph is None:
                print("请先处理文本!")
            else:
                showDirectedGraph(processed_graph)
        elif choice == "3":
            if processed_graph is None:
                print("请先处理文本!")
            else:
                queryBridgeWords(processed_graph, flag=0)
        elif choice == "4":
            if processed_graph is None:
                print("请先处理文本!")
            else:
                generateNewText(processed_graph)
        elif choice == "5":
            if processed_graph is None:
                print("请先处理文本!")
            else:
                calcShortestPath(processed_graph)
        elif choice == "6":
            if processed_graph is None:
                print("请先处理文本!")
            else:
                randomWalk(processed_graph)
        elif choice == "7":
            break
        else:
            print("无效的选项!")

if __name__ == "__main__":
    main()