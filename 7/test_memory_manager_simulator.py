from memory_manager_simulator import MemoryManagerSimulator
import unittest

class TestMemoryManagerSimulator(unittest.TestCase):
    def test_constructor(self):
        simulator = MemoryManagerSimulator()
        self.assertEqual(simulator.symbol_table, {})
    
    def test_reserve(self):
        simulator = MemoryManagerSimulator()

        simulator.reserve(["a", "b"])
        self.assertEqual(simulator.symbol_table["a"].value, "b")

        with self.assertRaises(Exception, msg="should raise exception when redeclaring name"):
            simulator.reserve(["a", "b"])
    
    def test_assign(self):
        simulator = MemoryManagerSimulator()

        with self.assertRaises(Exception, msg="should raise exception when assigning to an undefined name"):
            simulator.assign(["a", "b"])

        simulator.reserve(["a", "b"])
        simulator.assign(["c", "a"])
        self.assertEqual(simulator.symbol_table["c"], simulator.symbol_table["a"])
    
    def test_free(self):
        simulator = MemoryManagerSimulator()

        with self.assertRaises(Exception, msg="should raise exception when freeing an undefined name"):
            simulator.free(["a"])

        simulator.reserve(["a", "b"])
        simulator.free(["a"])
        self.assertEqual(simulator.symbol_table["a"].value, None)
    
    def test_print(self):
        simulator = MemoryManagerSimulator()

        with self.assertRaises(Exception, msg="should raise exception when printing an undefined name"):
            simulator.print(["a"])

        simulator.reserve(["a", "b"])
        self.assertEqual(simulator.print(["a"]), "b")

        simulator.free(["a"])
        with self.assertRaises(Exception, msg="should raise exception when printing a freed name"):
            simulator.print(["a"])
