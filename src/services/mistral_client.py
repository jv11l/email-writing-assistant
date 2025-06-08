from mistralai import Mistral
from ..settings.settings import Settings


class MistralAPIClient:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            print("Instantiating a new Mistral API Client...")
            cls.__instance = super().__new__(cls)
            config = Settings.get_config()
            api_key = config['api_key']
            if api_key is None:
                raise ValueError(
                    f"MISTRAL API KEY is {api_key}. Set your API KEY as environment variable!"
                )
            return Mistral(api_key=api_key)
