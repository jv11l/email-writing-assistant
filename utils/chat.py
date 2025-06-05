from mistralai import Mistral
import os

api_key = os.environ['MISTRAL_API_KEY']
client = Mistral(api_key=api_key)
model_small = 'mistral-small-2503' # latency optimised 24B-parameter pre-trained and instructed model

# Generate response
def chat_with_mistral(messages):
    chat_response = client.chat.complete(
        model=model_small,
        temperature=0.5,
        messages=messages,
        random_seed=42
    )
    return chat_response.choices[0].message.content