import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import task

class TestGreeting(unittest.TestCase):
    def test_name_is_string(self):
        self.assertIsInstance(task.name, str, "name must be a string")

    def test_age_is_int(self):
        self.assertIsInstance(task.age, int, "age must be an integer")

if __name__ == "__main__":
    unittest.main()
