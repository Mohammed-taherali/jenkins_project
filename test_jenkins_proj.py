import unittest
import jenkins_proj as jp

class TestJenkinsProj(unittest.TestCase):
    def test_add(self):
        self.assertEqual(jp.add(10, 5), 15)
        self.assertEqual(jp.add(-1, 1), 0)
        self.assertEqual(jp.add(-10, 11), 1)
        self.assertEqual(jp.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(jp.subtract(1, -1), 2)
        self.assertEqual(jp.subtract(15, 4), 11)
        self.assertEqual(jp.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(jp.multiply(10, 4), 40)
        self.assertEqual(jp.multiply(-2, -6), 12)
        self.assertEqual(jp.multiply(1, -4), -4)

    def test_divide(self):
        self.assertEqual(jp.divide(10, 5), 2)
        self.assertEqual(jp.divide(12, 1), 12)
        self.assertEqual(jp.divide(-4, 5), -0.80)

        with self.assertRaises(ValueError):
            jp.divide(10, 0)


if __name__ == "__main__":
    unittest.main()