from langchain.core_messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage(content="You are a helpful assistant that writes a poem based on the user's input."),
]