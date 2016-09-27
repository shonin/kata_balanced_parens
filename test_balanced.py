import balanced
import unittest

class TestBalanced(unittest.TestCase):
    def setUp(self):
        self.balance_checker = balanced.Balanced()

    def test_empty_string_is_balanced(self):
        self.assertTrue(self.balance_checker.answer(""))

    def test_single_parenthesis_is_unbalanced(self):
        self.assertFalse(self.balance_checker.answer("("))

    def test_pair_of_parens_is_balanced(self):
        self.assertTrue(self.balance_checker.answer("()"))

    def test_two_open_one_closed_paren_is_unbalanced(self):
        self.assertFalse(self.balance_checker.answer("(()"))

    def test_nested_balanced_parens_are_balanced(self):
        self.assertTrue(self.balance_checker.answer("(())"))

    def test_reversed_parens_are_unbalanced(self):
        self.assertFalse(self.balance_checker.answer(")("))

    def test_two_open_close_are_balanced(self):
        self.assertTrue(self.balance_checker.answer("()()"))

    def test_brackets_nested_in_parens_are_balanced(self):
        self.assertTrue(self.balance_checker.answer("([])"))

    def test_brackets_are_balanced(self):
        self.assertTrue(self.balance_checker.answer("[]"))

    def test_insane_number_of_parens(self):
        self.assertTrue(self.balance_checker.answer("((((((((((((((((((()))))))))))))))))))"))

def test_insane_number_of_parens(self):
        self.assertTrue(self.balance_checker.answer("(((((((((((((((((()))))))))))))))))))"))


if __name__ == '__main__':
    unittest.main()
