import os

class Settings:
    API_KEY: str = os.getenv('MISTRAL_API_KEY')
    MISTRAL_MODEL: str = 'mistral-small-2501' # latency optimised 24B-parameter pre-trained and instructed model
    API_TIMEOUT: int = 10e6
    
    @classmethod
    def get_config(cls) -> dict:
        return {
            'api_key': cls.API_KEY,
            'model': cls.MISTRAL_MODEL,
            # 'timeout_ms': cls.API_TIMEOUT,
        }
