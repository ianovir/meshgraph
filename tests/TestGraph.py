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

    def test_deleting_node(self):
        graph = Graph()
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(0, 0, 0, 1))
        graph.add_node(Node(1, 2, 3, 0))
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(5, -6, -2, 4))

        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)
        graph.add_edge(0, 4)
        graph.remove_node(graph.get_node(0))

        assert len(graph.nodes) == 4
        assert len(graph.nodes[0].neighbors) == 0
        assert len(graph.nodes[1].neighbors) == 0
        assert len(graph.nodes[2].neighbors) == 0
        assert len(graph.nodes[3].neighbors) == 0

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

    def test_add_edge(self):
        node_1 = Node(1, 1, 1)
        node_2 = Node(2, 2, 2)
        graph = Graph()
        graph.add_node(node_1)
        graph.add_node(node_2)

        graph.add_edge(0, 1)

        assert node_2 in graph.get_node(0).neighbors
        assert node_1 in graph.get_node(1).neighbors

    def test_copy_constructor_graph(self):
        node_1 = Node(1, 1, 1)
        node_2 = Node(2, 2, 2)
        graph = Graph()
        graph.add_node(node_1)
        graph.add_node(node_2)

        copy_graph = Graph(graph)

        assert len(copy_graph.nodes) == 2
        assert node_1 in copy_graph.nodes
        assert node_2 in copy_graph.nodes

    def test_copy_constructor_graph_nodes_independency(self):
        node_1 = Node(1, 1, 1)
        node_2 = Node(2, 2, 2)
        graph = Graph()
        graph.add_node(node_1)
        graph.add_node(node_2)

        copy_graph = Graph(graph)

        graph.subtract_nodes([node_2])
        graph.add_node(Node(3, 3, 3))
        graph.add_node(Node(4, 4, 4))

        assert len(copy_graph.nodes) == 2
        assert node_1 in copy_graph.nodes
        assert node_2 in copy_graph.nodes


if __name__ == "__main__":
    unittest.main()
    print("OK")
