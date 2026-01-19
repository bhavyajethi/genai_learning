from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage(content="You are a helpful assistant that writes a poem based on the user's input."),
    HumanMessage(content="Write a poem about the beauty of nature."),
]

chain = model | StrOutputParser()
response = chain.invoke(messages)
print(response)