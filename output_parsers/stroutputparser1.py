from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# OpenAI requires a paid plan to access their API, so this a just a placeholder and these exists no api key for this model.
model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)


# Start Program
#    ↓
# load_dotenv()
#    ↓
# .env file
#    ↓
# OPENAI_API_KEY loaded into os.environ
#    ↓
# ────────────────────────────────────────
#    ↓
# ChatOpenAI() instantiated
#    ↓
# (OpenAI client configured — NO API CALL YET)
#    ↓
# ────────────────────────────────────────
#    ↓
# PromptTemplate #1 created
# "Write a detailed report on {topic}"
#    ↓
# PromptTemplate #2 created
# "Write a 5 line summary on the following text"
#    ↓
# ────────────────────────────────────────
#    ↓
# StrOutputParser created
#    ↓
# (Used to convert AIMessage → string)
#    ↓
# ────────────────────────────────────────
#    ↓
# LCEL Chain constructed using `|`
# (template1 | model | parser | template2 | model | parser)
#    ↓
# (NO execution yet — just a pipeline definition)
#    ↓
# ────────────────────────────────────────
#    ↓
# chain.invoke({"topic": "black hole"})
#    ↓
# Execution starts HERE ⬇️
