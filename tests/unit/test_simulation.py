import unittest
from app.core.simulation import Simulation

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.simulation = Simulation()

    def test_initial_conditions(self):
        self.assertEqual(self.simulation.get_state(), "initialized")

    def test_run_simulation(self):
        result = self.simulation.run()
        self.assertTrue(result)

    def test_simulation_data(self):
        self.simulation.run()
        data = self.simulation.get_data()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()