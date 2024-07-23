import requests
def call_chatgpt(api_key, prompt, model="gpt-3.5-turbo"):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"


# Example usage
api_key = "sk-jL9pQw5OajxHAGwo4D6MaaFudfGZx3t61ZVhPdRIabG2X8XG"
prompt = "讲个笑话"

response = call_chatgpt(api_key, prompt)
print(response)
