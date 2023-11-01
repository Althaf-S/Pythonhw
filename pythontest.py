import unittest
<<<<<<< HEAD
from pythonhw import panagram
from pythonhw import palindrome
from pythonhw import freq
=======
from python_hw import panagram
from python_hw import palindrome
>>>>>>> 4d1003c (Implementation of palindrome testing)

class TestPanagram(unittest.TestCase):
    def testIsPanagram(self):
        sentence = "the quick brown fox jumpes over the lazy dog"
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
<<<<<<< HEAD
        empty = palindrome("")
        self.assertTrue(empty)
    def testSingleInputPalindrome(self):
        sentence = palindrome("a")
        self.assertTrue(sentence)
        
class TestFreq(unittest.TestCase):
    def testCasesensitiveFreq(self):
        sentence = "Hello World"
        self.assertTrue(freq(sentence))
    def testNormalFreq(self):
        sentence = "Hello World"
        self.assertTrue(freq(sentence))
    def testSymbolFreq(self):
        sentence = "Hello-w-o-rld"
        self.assertTrue(freq(sentence))
    def testNullInputDict(self):
        space = freq("")
        self.assertFalse(space)
        
=======
        sentence = palindrome("")
        self.assertTrue(sentence)
    def testSingleInputPalindrome(self):
        sentence = palindrome("a")
        self.assertTrue(sentence)


>>>>>>> 4d1003c (Implementation of palindrome testing)
if __name__ == "__main__":
  unittest.main()
   
        
