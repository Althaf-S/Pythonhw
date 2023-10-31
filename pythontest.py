import unittest
from python_hw import panagram
from python_hw import palindrome

class TestPanagram(unittest.TestCase):
    def testIsPanagram(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        self.assertTrue(panagram(sentence))
    def testIsNotPanagram(self):
        sentence = "the quick brown fox jumped over the lazy dog"
        self.assertFalse(panagram(sentence))
    def testNullInput(self):
        ret = panagram("")
        self.assertFalse(ret)
        
class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        sentence = "abba"
        self.assertTrue(palindrome(sentence))
    def testIsNotPalindrome(self):
        sentence = "abcde"
        self.assertFalse(palindrome(sentence))
    def testNullInput(self):
        sentence = palindrome("")
        self.assertTrue(sentence)
    def testSingleInputPalindrome(self):
        sentence = palindrome("a")
        self.assertTrue(sentence)


if __name__ == "__main__":
    unittest.main()
