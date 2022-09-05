from meshgraph.Node import Node
import unittest


class TestNode(unittest.TestCase):

    def test_node_creation_index(self):
        node_1 = Node(1, 1, 1, 52)
        assert node_1.index == 52

    def test_add_neighbor(self):
        node_1 = Node(1, 1, 1)
        node_2 = Node(2, 2, 2)
        node_1.add_neighbor(node_2)

        assert node_2 in node_1.neighbors
        assert node_1 not in node_2.neighbors

    def test_add_neighbor_idempotency(self):
        node_1 = Node(1, 1, 1)
        node_2 = Node(2, 2, 2)
        node_1.add_neighbor(node_2)
        node_1.add_neighbor(node_2)
        node_1.add_neighbor(node_2)

        assert len(node_1.neighbors) == 1
        assert node_2 in node_1.neighbors


if __name__ == "__main__":
    unittest.main()
    print("OK")
