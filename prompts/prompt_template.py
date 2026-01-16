from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
template2 = ChatPromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"]
)

parser = StrOutputParser()
chain2 = template2 | model | parser
response = chain2.invoke({"name": "Bhavya"})
print(response)