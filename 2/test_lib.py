import unittest
from lib import op, addParenthesis, show, eval

class TestMain(unittest.TestCase):
    def test_op(self):
        """test op"""

        self.assertEqual(op('+', 1, 2), 3, "should add")
        self.assertEqual(op('-', 1, 2), -1, "should subtract")
        self.assertEqual(op('*', 1, 2), 2, "should multiply")
        self.assertEqual(op('/', 1, 2), 0.5, "should divide")
    
    def test_addParenthesis(self):
        """ test addParenthesis"""

        # should never add parenthesis if op is +
        self.assertEqual(addParenthesis('+', ('+', '1 + 2'), 0), '1 + 2', "should not add parenthesis when the op is a sum and the first arg is a sum")
        self.assertEqual(addParenthesis('+', ('+', '1 + 2'), 1), '1 + 2', "should not add parenthesis when the op is a sum and the second arg is a sum")
        self.assertEqual(addParenthesis('+', ('-', '1 - 2'), 0), '1 - 2', "should not add parenthesis when the op is a sum and the first arg is a subtraction")
        self.assertEqual(addParenthesis('+', ('-', '1 - 2'), 1), '1 - 2', "should not add parenthesis when the op is a sum and the second arg is a subtraction")
        self.assertEqual(addParenthesis('+', ('*', '1 * 2'), 0), '1 * 2', "should not add parenthesis when the op is a sum and the first arg is a multiplication")
        self.assertEqual(addParenthesis('+', ('*', '1 * 2'), 1), '1 * 2', "should not add parenthesis when the op is a sum and the second arg is a multiplication")
        self.assertEqual(addParenthesis('+', ('/', '1 / 2'), 0), '1 / 2', "should not add parenthesis when the op is a sum and the first arg is a division")
        self.assertEqual(addParenthesis('+', ('/', '1 / 2'), 1), '1 / 2', "should not add parenthesis when the op is a sum and the second arg is a division")

        # should add parenthesis if op is - and second argument is sum or substraction
        self.assertEqual(addParenthesis('-', ('+', '1 + 2'), 1), '(1 + 2)', "should add parenthesis when the op is a subtraction and the second arg is a sum")
        self.assertEqual(addParenthesis('-', ('-', '1 - 2'), 1), '(1 - 2)', "should add parenthesis when the op is a subtraction and the second arg is a subtraction")
        
        # should not add parenthesis if op is - and first argument is sum or substraction
        self.assertEqual(addParenthesis('-', ('+', '1 + 2'), 0), '1 + 2', "should not add parenthesis when the op is a subtraction and the first arg is a sum")
        self.assertEqual(addParenthesis('-', ('-', '1 - 2'), 0), '1 - 2', "should not add parenthesis when the op is a subtraction and the first arg is a subtraction")

        # should not add parenthesis if op is - and either first or second argument is multiplication or division
        self.assertEqual(addParenthesis('-', ('*', '1 * 2'), 0), '1 * 2', "should not add parenthesis when the op is a subtraction and the first arg is a multiplication")
        self.assertEqual(addParenthesis('-', ('/', '1 / 2'), 0), '1 / 2', "should not add parenthesis when the op is a subtraction and the first arg is a division")
        self.assertEqual(addParenthesis('-', ('*', '1 * 2'), 1), '1 * 2', "should not add parenthesis when the op is a subtraction and the second arg is a multiplication")
        self.assertEqual(addParenthesis('-', ('/', '1 / 2'), 1), '1 / 2', "should not add parenthesis when the op is a subtraction and the second arg is a division")

        #should add parenthesis if op is * and either first or second argument is sum or subtraction
        self.assertEqual(addParenthesis('*', ('+', '1 + 2'), 0), '(1 + 2)', "should add parenthesis when the op is a multiplication and the first arg is a sum")
        self.assertEqual(addParenthesis('*', ('-', '1 - 2'), 0), '(1 - 2)', "should add parenthesis when the op is a multiplication and the first arg is a subtraction")
        self.assertEqual(addParenthesis('*', ('+', '1 + 2'), 1), '(1 + 2)', "should add parenthesis when the op is a multiplication and the second arg is a sum")
        self.assertEqual(addParenthesis('*', ('-', '1 - 2'), 1), '(1 - 2)', "should add parenthesis when the op is a multiplication and the second arg is a subtraction")

        #should not add parenthesis if op is * and either first or second argument is multiplication or division
        self.assertEqual(addParenthesis('*', ('*', '1 * 2'), 0), '1 * 2', "should not add parenthesis when the op is a multiplication and the first arg is a multiplication")
        self.assertEqual(addParenthesis('*', ('/', '1 / 2'), 0), '1 / 2', "should not add parenthesis when the op is a multiplication and the first arg is a division")
        self.assertEqual(addParenthesis('*', ('*', '1 * 2'), 1), '1 * 2', "should not add parenthesis when the op is a multiplication and the second arg is a multiplication")
        self.assertEqual(addParenthesis('*', ('/', '1 / 2'), 1), '1 / 2', "should not add parenthesis when the op is a multiplication and the second arg is a division")

        #should add parenthesis if op is / and either first or second argument is sum or subtraction
        self.assertEqual(addParenthesis('/', ('+', '1 + 2'), 0), '(1 + 2)', "should add parenthesis when the op is a division and the first arg is a sum")
        self.assertEqual(addParenthesis('/', ('-', '1 - 2'), 0), '(1 - 2)', "should add parenthesis when the op is a division and the first arg is a subtraction")
        self.assertEqual(addParenthesis('/', ('+', '1 + 2'), 1), '(1 + 2)', "should add parenthesis when the op is a division and the second arg is a sum")
        self.assertEqual(addParenthesis('/', ('-', '1 - 2'), 1), '(1 - 2)', "should add parenthesis when the op is a division and the second arg is a subtraction")

        #should add parenthesis if op is / and second argument is multiplication or division
        self.assertEqual(addParenthesis('/', ('*', '1 * 2'), 1), '(1 * 2)', "should add parenthesis when the op is a division and the second arg is a multiplication")
        self.assertEqual(addParenthesis('/', ('/', '1 / 2'), 1), '(1 / 2)', "should add parenthesis when the op is a division and the second arg is a division")

        #should not add parenthesis if op is / and first argument is multiplication or division
        self.assertEqual(addParenthesis('/', ('*', '1 * 2'), 0), '1 * 2', "should not add parenthesis when the op is a division and the first arg is a multiplication")
        self.assertEqual(addParenthesis('/', ('/', '1 / 2'), 0), '1 / 2', "should not add parenthesis when the op is a division and the first arg is a division")

    def test_show(self):
        """ test show """

        # when an invalid token is passed
        with self.assertRaises(ValueError, msg="should raise an error when an invalid token is passed"):
            show(['1', '#', '+'])

        # when not enough operands are passed for an operation
        with self.assertRaises(IndexError, msg="should raise an error when not enough operands exist for an operation"):
            show(['5', '+'])

        # when pre is false (default)
        self.assertEqual(show(['1', '2', '+',]), '1 + 2', "should transform postfix to infix")

        # when pre is true
        self.assertEqual(show(['+', '1', '2'], True), '1 + 2', "should transform prefix to infix")

    def test_eval(self):
        """ test eval """

        # when an invalid token is passed
        with self.assertRaises(ValueError, msg="should raise an error when an invalid token is passed"):
            eval(['1', '#', '+'])

        # when not enough operands are passed for an operation
        with self.assertRaises(IndexError, msg="should raise an error when not enough operands exist for an operation"):
            eval(['5', '+'])

        # when pre is false (default)
        self.assertEqual(eval(['1', '2', '+',]), 3, "should evaluate postfix")

        # when pre is true
        self.assertEqual(eval(['+', '1', '2'], True), 3, "should evaluate prefix")
