import time

import requests
history = []
while True:
    prompt = input("You: ")
    if not prompt.strip():
        continue
    if(prompt.lower() == "exit"):
        break;
    
    history.append(f"User: {prompt}")
    full_prompt = "\n".join(history)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:4b",
            "prompt": full_prompt,
            "stream": False
        }
    )
    aiResponse = response.json()
    print("\nAI:", aiResponse["response"])
    history.append(f"Ai: {aiResponse['response']}")
print("Exiting program....")