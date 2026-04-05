from openai import OpenAI, api_key
import openai

openai = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
response = openai.chat.completions.create(model="phi3:latest",messages=[{
    "role":"system",
    "content":"A Smart AI System which tell answers acturately and smart manner"
    },{
    "role":"user",
    "content":"tell me fun-fact"
}])
print(response.choices[0].message.content)

