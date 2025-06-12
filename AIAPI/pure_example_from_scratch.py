from aiml_api import AIML_API

api = AIML_API()

completion = api.chat.completions.create(
    model="google/gemma-3n-e4b-it",
    messages=[
        {"role": "user", "content": "Explain the importance of low-latency LLMs"},
    ],
    temperature=0.7,
    max_tokens=256,
)

response = completion.choices[0].message.content
print("AI:", response)