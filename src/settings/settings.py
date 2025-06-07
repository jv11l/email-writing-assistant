import os

class Settings:
    API_KEY: str = os.environ['MISTRAL_API_KEY']
    MODEL: str = 'mistral-small-2501' # latency optimised 24B-parameter pre-trained and instructed model
    API_TIMEOUT: int = 90
    MAX_RETRIES: int = 5
    
    @classmethod
    def get_config(cls) -> dict:
        return {
            'api_key': cls.API_KEY,
            'model': cls.MODEL,
            'timeout': cls.API_TIMEOUT,
            'max_retries': cls.MAX_RETRIES
        }
        
if __name__ == '__main__':
    print(Settings.get_config())
    