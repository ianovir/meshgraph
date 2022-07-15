from typing import List
from meshgraph.Node import Node


class Graph:
    """
    Undirected Graph

    ...

    Attributes
    ----------
    nodes : List[Node]
        nodes (or vertices) composing the graph

    Methods
    -------
    add_node(node)
        Adds new node to the graph
    subtract_node(sub_nodes)
        Subtracts a list of nodes from the existing nodes
    sort_nodes(sub_nodes)
        Sorts nodes by node index
    print()
        Prints all the nodes and their neighbors in a pretty format

    """

    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def get_node(self, index: int) -> Node:
        return self.nodes[index]

    def subtract_nodes(self, sub_nodes: List[Node]):
        self.nodes = list(set(self.nodes) - set(sub_nodes))
        self.sort_nodes()
        self.__reset_nodes_indexes()

    def __reset_nodes_indexes(self):
        if len(self.nodes) == 0:
            return
        offset = self.nodes[0].index
        for n in self.nodes:
            n.index = n.index - offset
      
    def sort_nodes(self):
        """Sort nodes collection by node index"""
        self.nodes = sorted(self.nodes, key=lambda n: n.index)

    def print(self):
        """Prints a pretty string representation of the current node and its neighbors."""
        for n in self.nodes:
            print(n)
            print("\tneighbors:" + str(n.neighbors))
