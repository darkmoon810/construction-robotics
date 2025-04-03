import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.models.chat import ChatMessage

class SlackService:
    def __init__(self):
        self.client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
        self.channel_id = os.getenv("SLACK_CHANNEL_ID")

    def get_messages(self, limit=100) -> list[ChatMessage]:
        try:
            response = self.client.conversations_history(
                channel=self.channel_id,
                limit=limit
            )
            return [
                ChatMessage(
                    sender=msg.get("user", "AI Agent"),
                    text=msg.get("text", ""),
                    timestamp=msg.get("ts", "")
                )
                for msg in response["messages"]
            ]
        except SlackApiError as e:
            print(f"Slack API Error: {e.response['error']}")
            return []