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

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schemas=schema)

template = PromptTemplate(
    template = "Give 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_instruction_variables = {"format_instruction":parser.get_format_instructions()}
)

chain = completion | template | parser

result = chain.invoke({"topic":"black hole"})

print(result)