from .capitalize import cap
import unittest

class TestCap(unittest.TestCase):

    def test_word(self):
        text = 'python'
        result = cap(text)
        self.assertEquals(result, 'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = cap(text)
        self.assertEquals(result, 'Monty Python')


if __name__ == "__main__":
    unittest.main()