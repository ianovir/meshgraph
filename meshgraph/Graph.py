import math

class Vec3 :

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def distance(self, other):
    dx = (self.x - other.x)**2
    dy = (self.y - other.y)**2
    dz = (self.z - other.z)**2
    return math.sqrt(dx + dy+ dz)

class Node :
  '''Graph node representing a vertex in space (coordinates [x,y,z]);
  contains a list of neighbors Node '''

  def __init__(self, x, y, z):
    self.pos = Vec3(x, y, z)
    self.index = -1
    self.neighbors = set()

  def add_neighbor(self, node):
    self.neighbors.add(node)

  def __str__(self):
     return "V" + str(self.index) \
     +"[" + str(self.pos.x ) \
     + "," + str(self.pos.y) \
     + "," + str(self.pos.z )\
     + "]"

  def __repr__(self):
    return str(self)

class Graph :
  '''Undirected Graph type, adjacency list representation'''

  def __init__(self):
    self.nodes = []

  def add_node (self, node):
    self.nodes.append(node)

  def get_node (self, index):
    return self.nodes[index]

  def subtract_nodes(self, subNodes):
    self.nodes = list(set(self.nodes) - set(subNodes))
    self.sort_nodes()
    self.__reset_nodes_indexes()

  def __reset_nodes_indexes(self):
    if len(self.nodes) == 0 : return
    offset = self.nodes[0].index
    for n in self.nodes:
      n.index = n.index - offset
      
  def sort_nodes(self):
    self.nodes = sorted(self.nodes, key=lambda n: n.index)

  def print(self):
    for n in self.nodes:
      print(n)
      print("  neighbors:" + str(n.neighbors))