import requests
from jigglewiggle import API_KEY

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = API_KEY

# Use a dictionary for headers
request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write python script for hello world",
    "max_tokens": 10,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

print(response.status_code)
print(response.text)  # Print the response content

if response.status_code == 200:
    print(response.json()["choices"][0])
else:
    print(f"Request failed with status code: {str(response.status_code)}")
