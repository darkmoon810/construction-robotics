import unittest
from app.core.agents import Agent  # Assuming there's an Agent class in agents.py

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent(name="TestAgent")

    def test_agent_initialization(self):
        self.assertEqual(self.agent.name, "TestAgent")

    def test_agent_response(self):
        response = self.agent.respond("Hello")
        self.assertIsInstance(response, str)  # Assuming the response is a string

    def test_agent_action(self):
        action = self.agent.perform_action("move_forward")
        self.assertTrue(action)  # Assuming perform_action returns True on success

if __name__ == '__main__':
    unittest.main()