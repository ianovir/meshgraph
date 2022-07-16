from meshgraph.Vec3 import Vec3
import unittest
import math


class TestVec3(unittest.TestCase):

    def test_constructor(self):
        v3 = Vec3(1.2, 3.4, 5.6)

        assert v3.x == 1.2
        assert v3.y == 3.4
        assert v3.z == 5.6

    def test_small_distance(self):
        a = Vec3(0.1, 0.002, 0.0006)
        b = Vec3(0.00756, 0.0012, -0.00243)

        assert math.isclose(a.distance(b), 0.0924931051, rel_tol=1e10, abs_tol=0.0)

    def test_big_distance(self):
        a = Vec3(1005.1, 9006.126, -6357)
        b = Vec3(3952.3, -9812.001, -7431.006)

        assert math.isclose(a.distance(b), 19077.771896, rel_tol=1e10, abs_tol=0.0)


if __name__ == "__main__":
    unittest.main()
    print("OK")
