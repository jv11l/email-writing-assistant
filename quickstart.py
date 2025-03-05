import os
from mistralai import Mistral

api_key = os.environ['MISTRAL_API_KEY']

model_small = 'mistral-small-2501'  # latency optimised 24B-parameter pre-trained and instructed model

client = Mistral(api_key=api_key)

# Text Generation

question = {
    'role': 'user',
    'content': 'What is the best French cheese?'
}

# NO STREAMING: client.chat.complete()
# chat_response = client.chat.complete(
#     model=model_small,
#     messages=[question]
# )

# print(chat_response.choices[0].message.content)

# WITH STREAMING: client.chat.stremam()

stream_response = client.chat.stream(
    model=model_small,
    messages=[question]
)

for chunk in stream_response:
    print(chunk.data.choices[0].delta.content)