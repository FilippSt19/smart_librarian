from openai import OpenAI
from app.config import OPENAI_API_KEY

print(OPENAI_API_KEY[:10])

client = OpenAI(api_key=OPENAI_API_KEY)

try:
    models = client.models.list()
    print("SUCCESS")
except Exception as e:
    print(type(e))
    print(e)