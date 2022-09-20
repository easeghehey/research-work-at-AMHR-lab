import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()

openai.organization = os.getenv('ORGANIZATION_ID')
openai.api_key = os.getenv('API_KEY')

prompt = "Write Java code for a function that creates a Magic The Gathering card that destroys all creatures with flying."

response = openai.Completion.create(engine="davinci",max_tokens=200, prompt=prompt, temperature=0.5, 
top_p=1.0, frequency_penalty=0.52,presence_penalty=0.5)

# Write to Json

jsonObject = json.dumps(response, indent = 4)

with open("output.json", "w") as outfile:
    outfile.write(jsonObject) 


file = open('text.txt', 'w')
file.write(response['choices'][0]['text'])

# print(response) # get the output