from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)

topic = input("Enter a topic")

formatted = prompt.format(topic=topic)

blog = llm.predict(formatted)

print("Generated blog title", blog)