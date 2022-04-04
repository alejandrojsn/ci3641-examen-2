import unittest
from tombstone import Tombstone

class TestTombstone(unittest.TestCase):
    def test_constructor(self):
        """ test constructor """
        t = Tombstone('value')
        self.assertEqual(t.value, 'value', "should return the value passed in the constructor")
    
    def test_free(self):
        """ test free """
        t = Tombstone('value')
        t.free()
        self.assertEqual(t.value, None, "should set the value to None")
