import requests
from os import environ

def chatgpt(prompt):
    # OpenAI connection configuration
    URL = "https://api.openai.com/v1/chat/completions"
    api_key = environ["OPENAI_API_KEY"]
    org = environ["OPENAI_ORG"]
    proj = environ["OPENAI_PROJ"]

    # AI model configuration
    model = "gpt-3.5-turbo"
    temperature = 0.2

    # Chat roles configuration
    system_content = "You are assisting with various tasks and advising how those tasks should be done."
    user_content = prompt

    # HTTP request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "OpenAI-Organization": org,
        "OpenAI-Project": proj
    }

    # HTTP request payload
    payload = {
        "model": model,
        "temperature" : temperature,
        "messages" : [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    }
    
    response = requests.post(URL, headers=headers, json=payload).json()
    return(response['choices'][0]['message']['content'])
