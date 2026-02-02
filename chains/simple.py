from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 5 interestin facts about {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")    


# the below code uses StrOutputParser
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'football'})

print("This is the stroutput parser result", result)



# the below code uses StructuredOutputParser
# schema = [
#     ResponseSchema(name="fact_1", description="fact 1 about the topic"),
#     ResponseSchema(name="fact_2", description="fact 2 about the topic"),
#     ResponseSchema(name="fact_3", description="fact 3 about the topic")
# ]

# parser = StructuredOutputParser.from_response_schemas(schemas=schema)

# template = PromptTemplate(
#     template = "Give 3 facts about {topic} \n {format_instruction}",
#     input_variables=['topic'],
#     partial_instruction_variables = {"format_instruction":parser.get_format_instructions()}
# )


# chain = model | template | parser

# result = chain.invoke({"topic":"black hole"})

# print("This result is of structured output parser", result)