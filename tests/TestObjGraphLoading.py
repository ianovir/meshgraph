from meshgraph import ObjLoader
from meshgraph.Vec3 import Vec3
import unittest


class TestObjGraphLoading(unittest.TestCase):

	def test_simple_obj_loading(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 0\n" + \
			"v -1 -1 0\n" + \
			"v -1 1 0\n" + \
			"v 2 2 0\n" + \
			"v 2 -2 0\n" + \
			"v -2 -2 0\n" + \
			"v -2 2 0\n" + \
			"f 1 2 3 4\n" + \
			"f 5 6 7 8"

		graph = ObjLoader.load_graph_from_string(obj)

		assert graph is not None

	def test_no_face(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 0\n" + \
			"v -1 -1 0\n" + \
			"v -1 1 0"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 4
		assert len(graph.nodes[0].neighbors) == 0
		assert len(graph.nodes[1].neighbors) == 0
		assert len(graph.nodes[2].neighbors) == 0
		assert len(graph.nodes[3].neighbors) == 0

	def test_nodes_coordinates(self):
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

		assert len(graph.nodes) == 8
		assert graph.nodes[0].pos == Vec3(1, 1, 0)
		assert graph.nodes[1].pos == Vec3(1, -1, 3)
		assert graph.nodes[2].pos == Vec3(-1, -1, -3)
		assert graph.nodes[3].pos == Vec3(-1, 1, 0)
		assert graph.nodes[4].pos == Vec3(2, 2, 0)
		assert graph.nodes[5].pos == Vec3(2, -2, 6)
		assert graph.nodes[6].pos == Vec3(-2, -2, -6)
		assert graph.nodes[7].pos == Vec3(-2, 2, 0)

	def test_nodes_coordinates_with_noisy_input(self):
		obj = "v        1 1 0\n" + \
			"v  1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v -1 1 0\n" + \
			"v 2 2 0\n" + \
			"v  2 -2 6\n" + \
			"g2 -2 6\n" + \
			"v -2 -2 -6\n" + \
			"v -2 2 0\n" + \
			"vn -2 2 0\n" + \
			"vn -2 2    0\n" + \
			"vn -2 2 0\n" + \
			"vn -2 2 0\n" + \
			"f        1 2 3 4\n" + \
			"f 5 6   7 8"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 8
		assert graph.nodes[0].pos == Vec3(1, 1, 0)
		assert graph.nodes[1].pos == Vec3(1, -1, 3)
		assert graph.nodes[2].pos == Vec3(-1, -1, -3)
		assert graph.nodes[3].pos == Vec3(-1, 1, 0)
		assert graph.nodes[4].pos == Vec3(2, 2, 0)
		assert graph.nodes[5].pos == Vec3(2, -2, 6)
		assert graph.nodes[6].pos == Vec3(-2, -2, -6)
		assert graph.nodes[7].pos == Vec3(-2, 2, 0)

	def test_nodes_indexes(self):
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

		assert len(graph.nodes) == 8
		assert graph.nodes[0].index == 0
		assert graph.nodes[1].index == 1
		assert graph.nodes[2].index == 2
		assert graph.nodes[3].index == 3
		assert graph.nodes[4].index == 4
		assert graph.nodes[5].index == 5
		assert graph.nodes[6].index == 6
		assert graph.nodes[7].index == 7

	def test_nodes_access_from_graph(self):
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

		assert len(graph.nodes) == 8
		assert graph.get_node(0).pos == Vec3(1, 1, 0)
		assert graph.get_node(1).pos == Vec3(1, -1, 3)
		assert graph.get_node(2).pos == Vec3(-1, -1, -3)
		assert graph.get_node(3).pos == Vec3(-1, 1, 0)
		assert graph.get_node(4).pos == Vec3(2, 2, 0)
		assert graph.get_node(5).pos == Vec3(2, -2, 6)
		assert graph.get_node(6).pos == Vec3(-2, -2, -6)
		assert graph.get_node(7).pos == Vec3(-2, 2, 0)

	def test_coincident_nodes_loading(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"f 1 2 3 \n" + \
			"f 4 5 6"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 6
		assert graph.nodes[0].pos == Vec3(1, 1, 0)
		assert graph.nodes[1].pos == Vec3(1, -1, 3)
		assert graph.nodes[2].pos == Vec3(-1, -1, -3)
		assert graph.nodes[3].pos == Vec3(1, 1, 0)
		assert graph.nodes[4].pos == Vec3(1, -1, 3)
		assert graph.nodes[5].pos == Vec3(-1, -1, -3)

	def test_neighbors_for_coincident_nodes_loading(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"f 1 2 3 \n" + \
			"f 4 5 6"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 6
		assert len(graph.nodes[0].neighbors) == 2
		assert len(graph.nodes[1].neighbors) == 2
		assert len(graph.nodes[2].neighbors) == 2
		assert len(graph.nodes[3].neighbors) == 2
		assert len(graph.nodes[4].neighbors) == 2
		assert len(graph.nodes[5].neighbors) == 2
		assert graph.nodes[2] in graph.nodes[0].neighbors
		assert graph.nodes[1] in graph.nodes[0].neighbors
		assert graph.nodes[0] in graph.nodes[1].neighbors
		assert graph.nodes[2] in graph.nodes[1].neighbors
		assert graph.nodes[1] in graph.nodes[2].neighbors
		assert graph.nodes[0] in graph.nodes[2].neighbors
		assert graph.nodes[5] in graph.nodes[3].neighbors
		assert graph.nodes[4] in graph.nodes[3].neighbors
		assert graph.nodes[3] in graph.nodes[4].neighbors
		assert graph.nodes[5] in graph.nodes[4].neighbors
		assert graph.nodes[4] in graph.nodes[5].neighbors
		assert graph.nodes[3] in graph.nodes[5].neighbors

	def test_nodes_from_redundant_faces(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v -1 1 0\n" + \
			"f 1 2 3 4\n" + \
			"f 4 3 2 1"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 4
		assert graph.nodes[0].pos == Vec3(1, 1, 0)
		assert graph.nodes[1].pos == Vec3(1, -1, 3)
		assert graph.nodes[2].pos == Vec3(-1, -1, -3)
		assert graph.nodes[3].pos == Vec3(-1, 1, 0)

	def test_neighbors_from_redundant_faces(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v -1 1 0\n" + \
			"f 1 2 3 4\n" + \
			"f 4 3 2 1"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 4
		assert len(graph.nodes[0].neighbors) == 2
		assert len(graph.nodes[1].neighbors) == 2
		assert len(graph.nodes[2].neighbors) == 2
		assert len(graph.nodes[3].neighbors) == 2
		assert graph.nodes[1] in graph.nodes[0].neighbors
		assert graph.nodes[3] in graph.nodes[0].neighbors
		assert graph.nodes[0] in graph.nodes[1].neighbors
		assert graph.nodes[2] in graph.nodes[1].neighbors
		assert graph.nodes[1] in graph.nodes[2].neighbors
		assert graph.nodes[3] in graph.nodes[2].neighbors
		assert graph.nodes[2] in graph.nodes[3].neighbors
		assert graph.nodes[0] in graph.nodes[3].neighbors

	def test_neighbors_from_non_regular_faces(self):
		obj = "v 1 1 0\n" + \
			"v 1 -1 3\n" + \
			"v -1 -1 -3\n" + \
			"v -1 1 0\n" + \
			"v 1 2 0\n" + \
			"v -2 3 4\n" + \
			"v -3 1 -2\n" + \
			"v -1 -1 -3\n" + \
			"v -1 1 0\n" + \
			"v 1 2 0\n" + \
			"v -2 3 4\n" + \
			"v -3 1 -2\n" + \
			"f 1 2 3 \n" + \
			"f 4 5 6 7 \n" + \
			"f 8 9 10 11 12"

		graph = ObjLoader.load_graph_from_string(obj)

		assert len(graph.nodes) == 12
		assert len(graph.nodes[0].neighbors) == 2
		assert len(graph.nodes[1].neighbors) == 2
		assert len(graph.nodes[2].neighbors) == 2
		assert len(graph.nodes[3].neighbors) == 2
		assert len(graph.nodes[4].neighbors) == 2
		assert len(graph.nodes[5].neighbors) == 2
		assert len(graph.nodes[6].neighbors) == 2
		assert len(graph.nodes[7].neighbors) == 2
		assert len(graph.nodes[8].neighbors) == 2
		assert len(graph.nodes[9].neighbors) == 2
		assert len(graph.nodes[10].neighbors) == 2
		assert len(graph.nodes[11].neighbors) == 2

		assert graph.nodes[2] in graph.nodes[0].neighbors
		assert graph.nodes[1] in graph.nodes[0].neighbors
		assert graph.nodes[0] in graph.nodes[1].neighbors
		assert graph.nodes[2] in graph.nodes[1].neighbors
		assert graph.nodes[1] in graph.nodes[2].neighbors
		assert graph.nodes[0] in graph.nodes[2].neighbors

		assert graph.nodes[6] in graph.nodes[3].neighbors
		assert graph.nodes[4] in graph.nodes[3].neighbors
		assert graph.nodes[3] in graph.nodes[4].neighbors
		assert graph.nodes[5] in graph.nodes[4].neighbors
		assert graph.nodes[4] in graph.nodes[5].neighbors
		assert graph.nodes[6] in graph.nodes[5].neighbors
		assert graph.nodes[5] in graph.nodes[6].neighbors
		assert graph.nodes[3] in graph.nodes[6].neighbors

		assert graph.nodes[11] in graph.nodes[7].neighbors
		assert graph.nodes[8] in graph.nodes[7].neighbors
		assert graph.nodes[7] in graph.nodes[8].neighbors
		assert graph.nodes[9] in graph.nodes[8].neighbors
		assert graph.nodes[8] in graph.nodes[9].neighbors
		assert graph.nodes[10] in graph.nodes[9].neighbors
		assert graph.nodes[9] in graph.nodes[10].neighbors
		assert graph.nodes[11] in graph.nodes[10].neighbors
		assert graph.nodes[10] in graph.nodes[11].neighbors
		assert graph.nodes[7] in graph.nodes[11].neighbors


if __name__ == "__main__":
	unittest.main()
	print("OK")
