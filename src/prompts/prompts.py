import os
from pathlib import Path

COMPONENTS_DIR = Path('src/prompts/components')
CONSTRAINTS = False

# Load prompts components and store them in a dictionary
prompt_components = {}

for component_file in os.listdir(COMPONENTS_DIR):
    component_key = component_file.split('.')[0]
    with open(COMPONENTS_DIR/component_file) as f:
        prompt_components[component_key] = f.read()

if CONSTRAINTS:
    pass
else:
    prompt_components['constraints'] = ""

# Define prompt using user message only
user_instructions = f"""You act as an email writing assistant.

{prompt_components['instructions']}

Follow the guidelines delimited by the XML tags <guidelines> </guidelines> 
for drafting your email and adhere to any specific constraints delimited by 
the XML tags <constraints> </constraints>.

<guidelines>\n{prompt_components['guidelines']}\n</guidelines>

<constraints>\n{prompt_components['constraints']}\n</constraints>
"""

messages_usr = [
    {'role': 'user', 'content': user_instructions},
]

# Define prompt using system and user instructions
system_prompt = f"""You act as an email writing assistant.
Follow the guidelines delimited by the XML tags <guidelines> </guidelines> 
for drafting your email and adhere to any specific constraints delimited by 
the XML tags <constraints> </constraints>.

<guidelines> {prompt_components['guidelines']} </guidelines>

<constraints> {prompt_components['constraints']} </constraints>
"""

user_instructions= f"""
{prompt_components['instructions']}
"""

# Define prompt messages without prefix
messages_sys_usr = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_instructions},
]

prefix = "Here is your email:"

# Define prompt messages with prefix
messages_sys_usr_pre = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_instructions},
    {'role': 'assistant', 'content': prefix,'prefix': True}
]

### TODO
# Add context
# Encapsulate into functions? class?