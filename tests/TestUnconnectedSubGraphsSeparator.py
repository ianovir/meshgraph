from meshgraph.Graph import Graph
from meshgraph.Graph import Node
from meshgraph.connectivity import UnconnectedSubGraphsSeparator
import unittest


class TestUnconnectedSubGraphsSeparator(unittest.TestCase):

    def test_single_graph(self):
        graph = Graph()
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(0, 0, 0, 1))
        graph.add_node(Node(1, 2, 3, 0))
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(5, -6, -2, 4))

        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        unconnected_graphs = UnconnectedSubGraphsSeparator.separate_unconnected_sub_graphs(graph)

        assert len(unconnected_graphs) == 1
        assert len(unconnected_graphs[0].nodes) == 5

    def test_two_graph(self):
        node1 = Node(-5, 5, -8, 7)
        node2 = Node(0, 0, 0, 1)
        node3 = Node(1, 2, 3, 0)
        node4 = Node(-5, 5, -8, 7)
        node5 = Node(5, -6, -2, 4)
        graph = Graph()
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.add_node(node4)
        graph.add_node(node5)

        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(3, 4)

        unconnected_graphs = UnconnectedSubGraphsSeparator.separate_unconnected_sub_graphs(graph)

        assert len(unconnected_graphs) == 2
        assert len(unconnected_graphs[0].nodes) == 3
        assert node1 in unconnected_graphs[0].nodes
        assert node2 in unconnected_graphs[0].nodes
        assert node3 in unconnected_graphs[0].nodes
        assert len(unconnected_graphs[1].nodes) == 2
        assert node4 in unconnected_graphs[1].nodes
        assert node5 in unconnected_graphs[1].nodes

    def test_all_isolated_vertices(self):
        node1 = Node(-5, 5, -8, 7)
        node2 = Node(0, 0, 0, 1)
        node3 = Node(1, 2, 3, 0)
        node4 = Node(-5, 5, -8, 7)
        node5 = Node(5, -6, -2, 4)
        graph = Graph()
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.add_node(node4)
        graph.add_node(node5)

        unconnected_graphs = UnconnectedSubGraphsSeparator.separate_unconnected_sub_graphs(graph)

        assert len(unconnected_graphs) == 5
        assert len(unconnected_graphs[0].nodes) == 1
        assert len(unconnected_graphs[1].nodes) == 1
        assert len(unconnected_graphs[2].nodes) == 1
        assert len(unconnected_graphs[3].nodes) == 1
        assert len(unconnected_graphs[4].nodes) == 1

    def test_retain_original_graph_nodes(self):
        graph = Graph()
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(0, 0, 0, 1))
        graph.add_node(Node(1, 2, 3, 0))
        graph.add_node(Node(-5, 5, -8, 7))
        graph.add_node(Node(5, -6, -2, 4))

        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        ignored = UnconnectedSubGraphsSeparator.separate_unconnected_sub_graphs(graph)

        assert len(graph.nodes) == 5

    if __name__ == "__main__":
        unittest.main()
        print("OK")
