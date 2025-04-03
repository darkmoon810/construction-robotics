# agents.py

class AIAgent:
    def __init__(self, name):
        self.name = name

    def communicate(self, message):
        # Placeholder for communication logic with the AI agent
        print(f"{self.name} received message: {message}")

def create_agent(name):
    return AIAgent(name)