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
    vertsIndexes.append(getVertIndexFromGroup(splitLine[i]))
  return vertsIndexes

def _link_mutual_neighbors(graph, a, b):
  graph.get_node(a).add_neighbor(graph.get_node(b))
  #undirected graph:
  graph.get_node(b).add_neighbor(graph.get_node(a))

def _solve_graph_neighbors(faceVertsIndexes, graph):
  for i in range(0, len(faceVertsIndexes)-1):
    link_mutual_neighbors(graph, faceVertsIndexes[i], faceVertsIndexes[i+1])    
  #link first and last (loop the face verts):
  link_mutual_neighbors(graph, faceVertsIndexes[0], faceVertsIndexes[-1])

def _parse_face_line(line, graph) :
  faceVertsIndexes = get_vertices_from_face_line(line)
  solve_graph_neighbors(faceVertsIndexes, graph)
  
def _parse_line(line, graph):
  line = line.strip()
  if line.startswith('v ') :
    parse_vertex_line(line, graph)
  elif line.startswith('f ') :
    parse_face_line(line, graph)

def load_graph_from_file(file_path):
  ''' Returns the graph '''

  graph = Graph()
  lines = load_file_content(file_path)
  for line in lines:
    parse_line(line, graph)
  print("Graph loaded, %s verts." % len(graph.nodes))
  return graph  