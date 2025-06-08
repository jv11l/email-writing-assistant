from src.services.api_service import chat_with_mistral
from src.prompts.prompts import messages_usr


if __name__ == '__main__':
    # Define the roles and contents of the prompt
    messages = messages_usr
    # Show full prompt send to the model
    for message in messages:
        print(message['content'])
    # Generate and save response
    assistant_response = chat_with_mistral(messages)
    with open("./responses/response.md", "w") as f:
        f.write(assistant_response)
        print(assistant_response)
