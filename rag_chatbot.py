import requests
with open("knowledge.txt" , "r") as file:
    knowledge = file.read()
while True:
    lines = knowledge.splitlines()
    question = input("You: ")

    word = question.lower().replace("?","").split()

    keyword = word[-1]

    if(question.lower() == "exit"):
        break

    relavent_text = ""
    for line in lines:
        if keyword in line.lower():
            relavent_text = line
            break
    
    if not relavent_text:
        print("No information found in the file")
        continue

    prompt = f""" 
    using this file 
    {relavent_text}
    Answering the question {question}
    """
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"qwen3:4b",
            "prompt":prompt,
            "stream":False
        }
    )
    aiResponse = response.json()

    print("Ai: " + aiResponse["response"])