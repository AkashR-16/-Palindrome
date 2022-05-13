from is_palindrome import is_palindrome
import unittest

class Testpalindrome(unittest.TestCase):
    def test_none_case(self):
        self.assertFalse(is_palindrome(None))

    def test_valid_case(self):
        self.assertTrue(is_palindrome("racecar"))
    def test_invalid_case(self):
        self.assertFalse(is_palindrome("lotion"))
    def test_valid_case_with_spaces(self):
        self.assertTrue(is_palindrome("Step on no pets"))
    def test_valid_case_empty_string(self):
        self.assertTrue(is_palindrome(" "))

    def test_invalid_case_caps_spacing(self):
        check_palindrome = is_palindrome("No lemon no melons")
        self.assertFalse(check_palindrome)

    def test_valid_case_caps(self):
        check_palindrome = is_palindrome("Racecar")
        self.assertTrue(check_palindrome)

    def test_invalid_case_empty(self):
        check_palindrome = is_palindrome("")
        self.assertFalse(check_palindrome)

    def test_valid_case_xtra_space(self):
        check_palindrome = is_palindrome("Step   on no pets")
        self.assertTrue(check_palindrome)

    def test_valid_case_with_splchr(self):
        check_palindrome = is_palindrome("Eva - can I see bees in a cave?")
        self.assertTrue(check_palindrome)

    def test_valid_case_splchr(self):
        check_palindrome = is_palindrome("A man, a plan, a canal: Panama!")
        self.assertTrue(check_palindrome)




if __name__ == '__main__':
    unittest.main()
