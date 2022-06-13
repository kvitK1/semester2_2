from graph_examples import figure_14_11 as example
from dfs import DFS
from dfs import DFS_complete

g = example()
print([(i.endpoints()[0].element(), i.endpoints()[1].element()) for i in g.edges()])
print("Number of vertices is", g.vertex_count())
#print("Vertices is", g.vertices())
print("Number of edges is", g.edge_count())

forest = DFS_complete(g)
for i, j in forest.items():
    print(i, j)