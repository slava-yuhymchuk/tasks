import requests

def chatgpt(prompt):
    # OpenAI connection configuration
    URL = "https://api.openai.com/v1/chat/completions"
    api_key = ""
    org = "org-goqFwnv5sW4plmQEpzT0jGGP"
    proj = "proj_EONnVwquY5PccBIoLO2Y4f1l"

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
    
    # print(response)
    # print(response['choices'][0]['message']['content'])
