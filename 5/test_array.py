from array_type import ArrayType
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
        t = TestType("int")

        s = ArrayType("myarray", t, 10)

        self.assertEqual(s.name, "myarray")
        self.assertEqual(s.type, t)
        self.assertEqual(s.length, 10)

    def test_size_packed(self):
        t = TestType("int", 4, 4, 0)

        s = ArrayType("myarray", t, 10)

        # when structs are packed
        self.assertEqual(s.size(False, True), 40, "size should equal the size of the type of the array multiplied by the length")

    def test_size_unpacked(self):
        t = TestType("char", 1, 2, 0)

        s = ArrayType("myarray", t, 10)

        # when structs are packed
        self.assertEqual(s.size(), 19, "size should take into account alignment")
    
    def test_alignment_packed(self):
        t = TestType("int", 4, 4, 0)

        s = ArrayType("myarray", t, 10)

        # when structs are packed
        self.assertEqual(s.alignment(False, True), 1, "alignment should be 1 when arrays are packed")

    def test_alignment_unpacked(self):
        t = TestType("int", 4, 3, 0)

        s = ArrayType("myarray", t, 10)

        # when structs are unpacked
        self.assertEqual(s.alignment(), 3, "alignment should be the alignment of the type when arrays are unpacked")
    
    def test_waste_packed(self):
        t = TestType("int", 4, 4, 10)

        s = ArrayType("myarray", t, 10)

        # when structs are packed
        self.assertEqual(s.waste(False, True), 100, "waste should be the waste of the type by the length when arrays are packed")

    def test_waste_unpacked(self):
        t = TestType("int", 3, 4, 1)

        s = ArrayType("mystruct", t, 10)

        # when structs are packed
        self.assertEqual(s.waste(), 19, "waste should be the size of the array minus the size of the type by the length plus the waste of the type by the length")


