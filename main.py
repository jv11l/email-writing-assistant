from mistralai import Mistral
import os
from pathlib import Path
from utils.chat import chat_with_mistral

# # Instantiate the Mistral Client
# api_key = os.environ['MISTRAL_API_KEY']
# model_small = 'mistral-small-2503'  # latency optimised 24B-parameter pre-trained and instructed model
# client = Mistral(api_key=api_key)

# Read components for drafting the email
components_dir = Path('components')
with open(components_dir/'guidelines.md') as f:
    guidelines = f.read()

with open(components_dir/'constraints.md') as f:
    constraints = f.read()

with open(components_dir/'instructions.md') as f:
    instructions = f.read()

# Define chat inputs
system_prompt = f"""You act as an email writing assistant.
Follow the guidelines delimited by the XML tags <guidelines> </guidelines> 
for drafting your email and adhere to any specific constraints delimited by 
the XML tags <constraints> </constraints>.

<guidelines> {guidelines} </guidelines>

<constraints> {constraints} </constraints>
"""

prefix = "Email writing assistant"

user_instructions = f"""
{instructions}
"""

messages=[
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_instructions},
    # {'role': 'assistant', 'content': prefix,'prefix': True}
]

if __name__ == '__main__':
    # Generate and save response
    assistant_response = chat_with_mistral(messages)
    with open("responses/response.md", "w") as f:
        f.write(assistant_response)