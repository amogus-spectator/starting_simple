import requests
import os
import json
import mistralai
from mistralai import Mistral

def get_api_key(path):
    """
    Reads the API key from a file.
    
    :param path: Path to the file containing the API key.
    :return: The API key as a string.
    """
    with open(path, 'r') as file:
        return file.read().strip()
def get_ai_response(prompt):
    
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-small-latest"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ]
    )

    return str(chat_response.choices[0].message.content) if chat_response.choices[0].message.content else None

def input_handling(input):
    if not input.isascii():
        return False
    if ("\\" in input or "\"" in input or "/" in input or ":" in input or "*" in input or "<" in input or ">" in input or "|" in input):
        return False
    if input == "":
        return False
    return True
    
def exit_program():
    print("Exiting the program.")
    exit(0)
    
def detect_exit_command(input):
    """
    Checks if the input command is an exit command and terminates the program if it is.

    :param input: The command input by the user.
    :return: True if the input is an exit command, otherwise None.
    """

    exit_commands = ["exit", "quit", "stop", "close"]
    if input.lower() in exit_commands:
        exit_program()
        return True
if __name__ == "__main__":
    
    while True:
        user_input = input("You: ")
        if input_handling(user_input):
            detect_exit_command(user_input)
            response = get_ai_response(user_input)
            if not response:
                print("No response from AI. Please try again.")
                continue
            print("AI: " + response)
        else:
            print("Invalid input. Please try again.")