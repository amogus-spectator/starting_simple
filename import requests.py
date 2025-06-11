import requests
import os
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
    if ("\\" in input or "\"" in input or "/" in input or ":" in input or "*" in input or "<" in input or ">" in input or "|" in input):
        return False
    if input == "":
        return False
    if (any(char in input for char in range(10000, 1114112))): #if any emoji are found in the input
        return False
    return True
    
def exit_program():
    print("Exiting the program.")
    exit(0)
    
def detect_exit_command(input):
/*************  ✨ Windsurf Command ⭐  *************/
    """
    Checks if the input command is an exit command and terminates the program if it is.

    :param input: The command input by the user.
    :return: True if the input is an exit command, otherwise None.
    """

/*******  eabdc810-5b1b-4161-9d83-cd4a8dceac77  *******/
    exit_commands = ["exit", "quit", "stop", "close"]
    if input.lower() in exit_commands:
        exit_program()
        return True
if __name__ == "__main__":
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Place your API key in a file named 'api_key.txt' in the same directory as this script
    api_key_path = os.path.join(current_directory, "api_key.txt")
    api_key = get_api_key(api_key_path)
    while True:
        user_input = input("You: ")
        if input_handling(user_input):
            detect_exit_command(user_input)
            response = get_ai_response(user_input)
            print("AI: " + response["choices"][0]["message"]["content"])
        else:
            print("Invalid input. Please try again.")