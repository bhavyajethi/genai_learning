from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from huggingface_hub import InferenceClient
import os

load_dotenv()

client = InferenceClient(
    api_key=os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"],
)


completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
)

# ROLE OF SCHEMA 
#  ResponseSchema defines the expected structure of the LLM output.
# Each ResponseSchema represents ONE key in the final response.
# Here, we are telling the model to return exactly 3 facts
# with fixed key names: fact_1, fact_2, and fact_3.
# This acts like a contract / blueprint for the output format.

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]


# ROLE OF STRUCTURED OUTPUT PARSER
# StructuredOutputParser is responsible for:
# 1) Generating format instructions for the LLM
#    (telling it to respond in valid JSON with the given keys)
# 2) Parsing the LLM response back into a Python dictionary
#    based on the schema defined above.

# from_response_schemas() is a factory method that:
# - Takes the list of ResponseSchema objects
# - Automatically builds formatting rules and parsing logic
# - Saves us from manually writing JSON instructions and parsers

parser = StructuredOutputParser.from_response_schemas(schemas=schema)


template = PromptTemplate(
    template = "Give 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    # ------------------ FORMAT INSTRUCTIONS ------------------
# parser.get_format_instructions() generates text instructions
# that are injected into the prompt so the LLM knows
# EXACTLY how to structure its output.

# Example instruction generated:
# "Respond ONLY in valid JSON with keys: fact_1, fact_2, fact_3"
    partial_instruction_variables = {"format_instruction":parser.get_format_instructions()}
)

chain = completion | template | parser

result = chain.invoke({"topic":"black hole"})

print(result)