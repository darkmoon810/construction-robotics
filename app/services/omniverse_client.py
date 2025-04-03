class ChatMessage:
    def __init__(self, user_id: str, message: str, timestamp: str):
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "message": self.message,
            "timestamp": self.timestamp
        }