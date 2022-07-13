from meshgraph.Graph import Graph
from meshgraph.Graph import Node

def _load_file_content(path):
  with open(path) as f:
    lines = [line for line in f]
    return lines

def _parse_vertex_line(line, graph):
  coordinates = line.split()
  newNode = Node(float(coordinates[1]),
                 float(coordinates[2]),
                 float(coordinates[3]))
  newNode.index = len(graph.nodes)
  graph.add_node(newNode)

def _getVertIndexFromGroup(vertGroup) :
  strIndex = vertGroup.split('/')[0]
  return int(strIndex)-1

def _get_vertices_from_face_line(line):
  splitLine = line.split()
  vertsIndexes = []
  for i in range(1, len(splitLine)):
    vertsIndexes.append(_getVertIndexFromGroup(splitLine[i]))
  return vertsIndexes

def _link_mutual_neighbors(graph, a, b):
  graph.get_node(a).add_neighbor(graph.get_node(b))
  #undirected graph:
  graph.get_node(b).add_neighbor(graph.get_node(a))

def _solve_graph_neighbors(faceVertsIndexes, graph):
  for i in range(0, len(faceVertsIndexes)-1):
    _link_mutual_neighbors(graph, faceVertsIndexes[i], faceVertsIndexes[i+1])    
  #link first and last (loop the face verts):
  _link_mutual_neighbors(graph, faceVertsIndexes[0], faceVertsIndexes[-1])

def _parse_face_line(line, graph) :
  faceVertsIndexes = _get_vertices_from_face_line(line)
  _solve_graph_neighbors(faceVertsIndexes, graph)
  
def _parse_line(line, graph):
  line = line.strip()
  if line.startswith('v ') :
    _parse_vertex_line(line, graph)
  elif line.startswith('f ') :
    _parse_face_line(line, graph)

def _fill_graph_from_lines(lines, graph):
  for line in lines:
    _parse_line(line, graph)
  print("Graph loaded, %s verts." % len(graph.nodes))
    

def load_graph_from_string(content):
  graph = Graph()
  _fill_graph_from_lines(content.splitlines(), graph)
  return graph

def load_graph_from_file(file_path):
  graph = Graph()
  lines = _load_file_content(file_path)
  _fill_graph_from_lines(lines, graph)
  return graph