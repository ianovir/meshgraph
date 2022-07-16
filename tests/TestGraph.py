from meshgraph.Graph import Graph
from meshgraph.Node import Node
import unittest
import math


class TestGraph(unittest.TestCase):

    def test_sorting_nodes(self):
        graph = Graph()
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(0, 0, 0, 1))
        graph.add_node(Node(1, 2, 3, 0))
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(5, -6, -2, 4))

        graph.sort_nodes()

        assert graph.nodes[0].index == 0
        assert graph.nodes[1].index == 1
        assert graph.nodes[2].index == 4
        assert graph.nodes[3].index == 7
        assert graph.nodes[4].index == 7

    def test_subtracting_nodes(self):
        node_7 = Node(-5, 5, -8, 7)
        node_1 = Node(0, 0, 0, 1)
        node_0 = Node(1, 2, 3, 0)
        node_4 = Node(5, -6, -2, 4)
        node_2 = Node(5, 7, -3, 2)
        graph = Graph()
        graph.add_node(node_7)
        graph.add_node(node_1)
        graph.add_node(node_0)
        graph.add_node(node_4)
        graph.add_node(node_2)

        graph.subtract_nodes([node_7, node_0, node_2])

        assert node_1 in graph.nodes
        assert node_4 in graph.nodes

    def test_subtracting_nodes_sorted(self):
        node_7 = Node(-5, 5, -8, 7)
        node_1 = Node(0, 0, 0, 1)
        node_0 = Node(1, 2, 3, 0)
        node_4 = Node(5, -6, -2, 4)
        node_2 = Node(5, 7, -3, 2)
        graph = Graph()
        graph.add_node(node_7)
        graph.add_node(node_1)
        graph.add_node(node_0)
        graph.add_node(node_4)
        graph.add_node(node_2)

        graph.subtract_nodes_sorted([node_7, node_0, node_2])

        assert graph.nodes[0].index == 1
        assert graph.nodes[1].index == 4

    def test_reset_nodes(self):
        node_7 = Node(-5, 5, -8, 7)
        node_1 = Node(0, 0, 0, 1)
        node_9 = Node(1, 2, 3, 9)
        node_4 = Node(5, -6, -2, 4)
        node_2 = Node(5, 7, -3, 2)
        graph = Graph()
        graph.add_node(node_7)
        graph.add_node(node_1)
        graph.add_node(node_9)
        graph.add_node(node_4)
        graph.add_node(node_2)

        graph.reset_nodes_indexes()

        assert graph.nodes[0].index == 0
        assert graph.nodes[1].index == 1
        assert graph.nodes[2].index == 2
        assert graph.nodes[3].index == 3
        assert graph.nodes[4].index == 4


if __name__ == "__main__":
    unittest.main()
    print("OK")
