from meshgraph import ObjLoader

import unittest

class TestStringMethods(unittest.TestCase):

	def test_simple_load_test(self):
		obj = "v 1 1 0\n"+\
		"v 1 -1 0\n"+\
		"v -1 -1 0\n"+\
		"v -1 1 0\n"+\
		"v 2 2 0\n"+\
		"v 2 -2 0\n"+\
		"v -2 -2 0\n"+\
		"v -2 2 0\n"+\
		"f 1 2 3 4\n"+\
		"f 4 3 2 1\n"+\
		"f 5 6 7 8"

		graph = ObjLoader.load_graph_from_string(obj)

		assert graph is not None
		assert len(graph.nodes) == 8



if __name__ == "__main__":
	unittest.main()
	print("OK")