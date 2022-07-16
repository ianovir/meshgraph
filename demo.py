from meshgraph import ObjLoader

obj = "v 1 1 0\n" + \
      "v 1 -1 3\n" + \
      "v -1 -1 -3\n" + \
      "v -1 1 0\n" + \
      "v 2 2 0\n" + \
      "v 2 -2 6\n" + \
      "v -2 -2 -6\n" + \
      "v -2 2 0\n" + \
      "f 1 2 3 4\n" + \
      "f 5 6 7 8"

graph = ObjLoader.load_graph_from_string(obj)
print(graph.nodes[0].index)
