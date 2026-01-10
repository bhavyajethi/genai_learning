from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
llm = model | StrOutputParser()
# .invoke calls the model with a prompt and returns the response
message = llm.invoke("What is the capital of India")
print(message)



# OPENAI DOESNT PROVIDE FREE API CREDITS SO THIS IS CODE IS JUST FOR REFERENCE
model = OpenAI(model="gpt-3.5-turbo-instruct")
llm_1 = model | StrOutputParser()
result = model.invoke("Explain the theory of relativity in simple terms.")
print(result)