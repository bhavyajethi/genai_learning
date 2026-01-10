from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# DONT USE THIS CODE AS OPENAI DOESNT PROVIDE FREE API CREDITS SO THIS IS CODE IS JUST FOR REFERENCE
load_dotenv()
# temperature is a parameter to control the randomness of the model's output. It affects the creativity checks the determinism of the responses. Max completion tokens limits the length of the response.
model = ChatOpenAI(model_name="gpt-4", temperature=0.7, max_completion_tokens=100)
chain = model | StrOutputParser()
# .invoke calls the model with a prompt and returns the response
result = chain.invoke("Write a 5 line poem on football.")
print(result)