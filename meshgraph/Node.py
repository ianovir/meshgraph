from meshgraph.Vec3 import Vec3


class Node:
    """
    Node representing a vertex in Euclidian space

    ...

    Attributes
    ----------
    pos : Vec3
        The coordinates of the Node
    neighbors : Set[Node]
        The set containing the neighbors of the current node

    Methods
    -------
    add_neighbor(node: Node)
        Adds new node to the neighbors

    """

    def __init__(self, x, y, z):
        self.pos = Vec3(x, y, z)
        self.index = -1
        self.neighbors = set()

    def add_neighbor(self, node: 'Node'):
        """Add new Node instance to neighbors"""
        self.neighbors.add(node)

    def __str__(self):
        return "V" + str(self.index) \
            + "[" + str(self.pos.x) \
            + "," + str(self.pos.y) \
            + "," + str(self.pos.z)\
            + "]"

    def __repr__(self):
        return str(self)
