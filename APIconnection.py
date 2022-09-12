import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.organization = os.getenv('ORGANIZATION_ID')
openai.api_key = os.getenv('API_KEY')

prompt = "Who won the last football world cup?"

response = openai.Completion.create(engine="davinci",max_tokens=25, prompt=prompt, temperature=0, 
top_p=1, frequency_penalty=0,presence_penalty=0)

print(response) # get the output