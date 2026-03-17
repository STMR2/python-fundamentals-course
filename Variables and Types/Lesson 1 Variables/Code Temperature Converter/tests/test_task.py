import unittest
import task

class TestTemperature(unittest.TestCase):
    def test_fahrenheit(self):
        self.assertAlmostEqual(task.fahrenheit, 77.0,
            msg="For celsius=25, fahrenheit must be 77.0")

if __name__ == "__main__":
    unittest.main()
