"""testing algorithms"""

from bfs import BFS_complete
from dfs import DFS_complete
from graph import Graph
from topological_sort import topological_sort


file_path = 'stanford_cs.txt'

def read_file(path):
    """Func to read file and write it to graph."""
    graph_data = {}
    with open(path, "r") as file:
        file = file.readlines()[1:]
        for line in file:
            inx = line.find(" ")
            graph_data[line[:inx]] = "".join(list(filter(lambda x: (x not in ("(", ")", " ")),
            list(line[inx+1:])))).strip().split(",")
    g = Graph()
    for key, val in graph_data.items():
        g.insert_vertex(key)
    for key, val in graph_data.items():
        for v in val:
            if v != 'none':
                piece1 = ""
                piece2 = ""
                for i in g.vertices():
                    if v == i.element():
                        piece1 = i
                    if key == i.element():
                        piece2 = i
                g.insert_edge(piece1, piece2)
    return g

def bfs_test(graf):
    """Tests BFS."""
    print("BFS testing ...")
    bfs_graf = BFS_complete(graf)
    assert len(bfs_graf) == 24
    elements = [el.element() for el in bfs_graf]
    assert elements[-1] == "ENGR40M"
    string = "->".join(el.element() for el in bfs_graf)
    print(string)
    for i, j in bfs_graf.items():
        print(i, j)

def dfs_test(graf):
    """Tests DFS."""
    print("DFS testing ...")
    dfs_graf = DFS_complete(graf)
    assert len(dfs_graf) == 24
    elements = [el.element() for el in dfs_graf]
    assert elements[0] == "MATH19"
    string = "->".join(el.element() for el in dfs_graf)
    print(string)
    for i, j in dfs_graf.items():
        print(i, j)

def topological_sort_test(graf):
    """Tests topological sort."""
    top_graf = topological_sort(graf)
    if top_graf:
        print("Topological sort testing ...")
        for key in top_graf:
            print(key)

if __name__ == "__main__":
    gr = read_file(file_path)
    bfs_test(gr)
    dfs_test(gr)
    topological_sort_test(gr)
