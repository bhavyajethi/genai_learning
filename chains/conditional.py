from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description = "Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instructions}",
    input_variables = ['feedback'],
    partial_variables = {'format_instructions' : parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)


prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: 'x could not find sentiment')
)

chain = classifier_chain | branch_chain 

print(chain.invoke({"feedback":"This is an amazing movie"}))

chain.get_graph().print_ascii()


# BELOW IS A GRAPHICAL REPRESENTATION OF THE WORKFLOW STEPWISE.
#     +-------------+      
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#       +----------+
#       | ChatGroq |
#       +----------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+