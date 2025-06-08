from src.services.mistral_client import MistralAPIClient
from ..settings.settings import Settings


config: dict = Settings.get_config()
model: str = config['model']
client = MistralAPIClient()

def chat_with_mistral(messages) -> str:
    chat_response = client.chat.complete(
        model=model,
        temperature=0.5,
        messages=messages,
        random_seed=42
    )
    return chat_response.choices[0].message.content
