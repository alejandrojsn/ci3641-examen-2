from struct_type import StructType
from type import Type
import unittest

class TestType(Type):
    def __init__(self, name, size = 1, alignment = 1, waste = 0):
        super().__init__(name)
        self._size = size
        self._alignment = alignment
        self._waste = waste
    
    def size(self, packed_structs = False, packed_arrays = False):
        return self._size
    
    def alignment(self, packed_structs = False, packed_arrays = False):
        return self._alignment
    
    def waste(self, packed_structs = False, packed_arrays = False):
        return self._waste

class TestStruct(unittest.TestCase):
    def test_constructor(self):
        t1 = TestType("int")
        t2 = TestType("char")

        s = StructType("mystruct", [t1, t2])

        self.assertEqual(s.name, "mystruct")
        self.assertEqual(s.types, [t1, t2])

    def test_size_packed(self):
        t1 = TestType("int", 4, 4, 0)
        t2 = TestType("char", 1, 2, 0)
        t3 = TestType("boolean", 1, 1, 0)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are packed
        self.assertEqual(s.size(True), 6, "size should equal the sum of the size of the types of the struct")

    def test_size_unpacked(self):
        t1 = TestType("char", 1, 2, 0)
        t2 = TestType("int", 4, 4, 0)
        t3 = TestType("boolean", 1, 1, 0)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are packed
        self.assertEqual(s.size(), 9, "size should take into account alignment")
    
    def test_alignment_packed(self):
        t1 = TestType("int", 4, 4, 0)
        t2 = TestType("char", 1, 2, 0)
        t3 = TestType("boolean", 1, 1, 0)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are packed
        self.assertEqual(s.alignment(True), 1, "alignment should be 1 when structs are packed")

    def test_alignment_unpacked(self):
        t1 = TestType("int", 4, 3, 0)
        t2 = TestType("char", 1, 5, 0)
        t3 = TestType("boolean", 1, 7, 0)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are unpacked
        self.assertEqual(s.alignment(), 105, "alignment should be lcm of the alignment of the struct types when structs are unpacked")
    
    def test_waste_packed(self):
        t1 = TestType("int", 4, 4, 10)
        t2 = TestType("char", 1, 2, 42)
        t3 = TestType("boolean", 1, 1, 69)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are packed
        self.assertEqual(s.waste(True), 121, "waste should be the sum of the waste of the types when structs are packed")

    def test_waste_unpacked(self):
        t1 = TestType("int", 4, 4, 1)
        t2 = TestType("char", 5, 5, 1)
        t3 = TestType("boolean", 4, 5, 1)

        s = StructType("mystruct", [t1, t2, t3])

        # when structs are packed
        self.assertEqual(s.waste(), 4, "waste should be the size of the struct minus the sum of the size of the types plus the sum of waste of the types when structs are unpacked")


