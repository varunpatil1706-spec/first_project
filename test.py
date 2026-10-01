from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b")

print("my first chatbot")

history=[]

while True:
    prompt=input("user:")
    history.append( prompt)
    if prompt=="exit":
        break
   
    responce=llm.invoke(history)
    history.append(responce)
    print(responce.content)