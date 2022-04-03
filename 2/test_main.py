import unittest
from unittest.mock import patch
from main import run

class TestMain(unittest.TestCase):
    def test_run(self):
        """ test run """

        # when an action is not specified in the input
        with self.assertRaises(ValueError, msg="should raise an error when an action is not specified in the input"):
            run("")
        
        # when an invalid action is specified in the input
        with self.assertRaises(ValueError, msg="should raise an error when an invalid action is specified in the input"):
            run("invalid")
        
        # when action is SALIR
        with self.assertRaises(SystemExit, msg="should raise a SystemExit when action is SALIR"):
            run("SALIR")
        
        # when action is EVAL or MOSTRAR but order is invalid
        with self.assertRaises(ValueError, msg="should raise an error when action is EVAL but order is invalid"):
            run("EVAL invalid")

        with self.assertRaises(ValueError, msg="should raise an error when action is MOSTRAR but order is invalid"):
            run("MOSTRAR invalid")
        
        # when action is EVAL or MOSTRAR and order is valid but no expression is passed
        with self.assertRaises(ValueError, msg="should raise an error when action is EVAL but no expression is passed"):
            run("EVAL POST")
        
        with self.assertRaises(ValueError, msg="should raise an error when action is MOSTRAR but no expression is passed"):
            run("MOSTRAR POST")

        # when action is EVAL and order is POST and expression is passed
        self.assertEqual(run("EVAL POST 3 2 +"), 5, "should return the result of eval")

        # when action is EVAL and order is PRE and expression is passed
        self.assertEqual(run("EVAL PRE + 3 2"), 5, "should return the result of eval")

        # when action is MOSTRAR and order is POST and expression is passed
        self.assertEqual(run("MOSTRAR POST 3 2 +"), '3 + 2', "should return the result of show")

        # when action is MOSTRAR and order is PRE and expression is passed
        self.assertEqual(run("MOSTRAR PRE + 3 2"), '3 + 2', "should return the result of show")





