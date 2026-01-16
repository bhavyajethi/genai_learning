from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# from langchain.memory import ConversationBufferMemory

load_dotenv()

# memory = ConversationBufferMemory()
# Chat history is mainttained to have a continuous conversation with the model and remember previous inputs and outputs.
chat_history = []
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    chain = model | StrOutputParser()
    response = chain.invoke(chat_history)
    chat_history.append(response)
    print("AI:", response)