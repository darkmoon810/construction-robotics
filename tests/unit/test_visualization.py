import unittest
from app.core.visualization import generate_plot

class TestVisualization(unittest.TestCase):

    def test_generate_plot(self):
        # Test with sample data
        data = [1, 2, 3, 4, 5]
        result = generate_plot(data)
        self.assertIsNotNone(result)
        self.assertIn('plot', result)  # Assuming the function returns a dict with a 'plot' key

if __name__ == '__main__':
    unittest.main()