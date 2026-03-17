import unittest
import task

class TestStringOps(unittest.TestCase):
    def test_char_count(self):
        self.assertEqual(task.char_count, 18,
            msg="char_count should be 18")

    def test_upper(self):
        self.assertEqual(task.upper_sentence, "HELLO WORLD PYTHON",
            msg="upper_sentence should be 'HELLO WORLD PYTHON'")

    def test_dashed(self):
        self.assertEqual(task.dashed, "hello-world-python",
            msg="dashed should be 'hello-world-python'")

if __name__ == "__main__":
    unittest.main()
