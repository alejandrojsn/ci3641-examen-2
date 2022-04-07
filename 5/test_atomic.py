import unittest
from atomic import Atomic

class TestAtomic(unittest.TestCase):
    def test_constructor(self):
        a = Atomic("int", 4, 4)

        self.assertEqual(a.name, "int")
        self.assertEqual(a.representation, 4)
        self.assertEqual(a._alignment, 4)

    def test_size(self):
        a = Atomic("int", 4, 4)

        self.assertEqual(a.size(), 4)
    
    def test_alignment(self):
        a = Atomic("int", 4, 4)

        self.assertEqual(a.alignment(), 4)
    
    def test_waste(self):
        a = Atomic("int", 4, 4)

        self.assertEqual(a.waste(), 0)
