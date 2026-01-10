from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
# temperature is a parameter to control the randomness of the model's output. It affects the creativity checks the determinism of the responses. Max output tokens limits the length of the response.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.5, max_output_tokens=100)
chain = model | StrOutputParser()
messages = [
    (
        "system",
        "You are a helpful assistant that writes a poem based on the user's input.",
    ),
    ("human", "Football."),
]
# .invoke calls the model with a prompt and returns the response
# print(type(messages))
ai_msg = chain.invoke(messages)
print(ai_msg)