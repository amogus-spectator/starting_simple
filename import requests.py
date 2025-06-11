import requests
import json

def get_api_key(path):
    """
    Reads the API key from a file.
    
    :param path: Path to the file containing the API key.
    :return: The API key as a string.
    """
    with open(path, 'r') as file:
        return file.read().strip()
def get_ai_response(prompt):
    response = requests.post(
    url="https://api.aimlapi.com/chat/completions",
    headers={
        "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
        "Content-Type": "application/json",
    },
    data=json.dumps(
        {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "max_tokens": 512,
            "stream": False,
        }
    ),
)

    response.raise_for_status()
    return response.json()

def input_handling(input):
    if ("\\" in input or "\"" in input or "/" in input or ":" in input or "*" in input or "<" in input or ">" in input or "|" in input or "?" in input):
        return False
    if input == "":
        return False
    if (any(char in input for char in range(10000, 1114112))): #if any emoji are found in the input
        return False
    return True
    
get_ai_response("Hello, how are you?")  # Example usage of the function