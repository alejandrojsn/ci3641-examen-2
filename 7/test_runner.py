from runner import Runner
from memory_manager_simulator import MemoryManagerSimulator
import unittest
from unittest.mock import patch

class TestRunner(unittest.TestCase):
    def test_constructor(self):
        simulator = MemoryManagerSimulator()
        runner = Runner(simulator)
        self.assertEqual(runner.simulator, simulator)
    
    def test_run(self):
        with patch('memory_manager_simulator.MemoryManagerSimulator') as mock:
            mocked_simulator = mock.return_value

            runner = Runner(mocked_simulator)

            runner.run("RESERVAR a b")
            mocked_simulator.reserve.assert_called_with(["a", "b"])

            runner.run("ASIGNAR c a")
            mocked_simulator.assign.assert_called_with(["c", "a"])

            runner.run("LIBERAR a")
            mocked_simulator.free.assert_called_with(["a"])

            runner.run("IMPRIMIR a")
            mocked_simulator.print.assert_called_with(["a"])

            self.assertEqual(runner.run(""), "unknown action: ")

            mocked_simulator.reserve.side_effect = Exception("reserve exception")
            self.assertEqual(runner.run("RESERVAR a b"), "reserve exception")

            with self.assertRaises(SystemExit, msg="should quit"):
                runner.run("SALIR")
