from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os 
from huggingface_hub import InferenceClient


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)


model = ChatHuggingFace(llm=llm)


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

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)




# Start Program
#    ↓
# load_dotenv()
#    ↓
# .env file
#    ↓
# HUGGINGFACEHUB_API_TOKEN loaded into os.environ
#    ↓
# ────────────────────────────────────────
#    ↓
# HuggingFaceEndpoint created
# (repo_id = mistralai/Mistral-7B-Instruct-v0.2)
#    ↓
# (No API call yet — config only)
#    ↓
# ────────────────────────────────────────
#    ↓
# ChatHuggingFace wrapper created
#    ↓
# LLM ready to accept prompts
#    ↓
# ────────────────────────────────────────
#    ↓
# PromptTemplate #1 created
# ("Write a detailed report on {topic}")
#    ↓
# PromptTemplate #2 created
# ("Write a 5 line summary on {text}")
#    ↓
# ────────────────────────────────────────
#    ↓
# template1.invoke({"topic": "black hole"})
#    ↓
# Prompt #1 formatted
# "Write a detailed report on black hole"
#    ↓
# ────────────────────────────────────────
#    ↓
# model.invoke(prompt1)
#    ↓
# ChatHuggingFace.invoke()
#    ↓
# HuggingFaceEndpoint.invoke()
#    ↓
# HTTP POST request
#    ↓
# Hugging Face Inference API
#    ↓
# mistralai/Mistral-7B-Instruct-v0.2
#    ↓
# Text generation (Detailed Report)
#    ↓
# LangChain wraps output → AIMessage
#    ↓
# result.content (long report)
#    ↓
# ────────────────────────────────────────
#    ↓
# template2.invoke({"text": result.content})
#    ↓
# Prompt #2 formatted
# "Write a 5 line summary on the following text..."
#    ↓
# ────────────────────────────────────────
#    ↓
# model.invoke(prompt2)
#    ↓
# ChatHuggingFace.invoke()
#    ↓
# HuggingFaceEndpoint.invoke()
#    ↓
# HTTP POST request
#    ↓
# Hugging Face Inference API
#    ↓
# mistralai/Mistral-7B-Instruct-v0.2
#    ↓
# Text generation (5-line summary)
#    ↓
# LangChain wraps output → AIMessage
#    ↓
# result1.content
#    ↓
# ────────────────────────────────────────
#    ↓
# print(result1.content)
#    ↓
# End Program
