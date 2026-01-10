# openai embedding models require paid api credits to this code is just for reference

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = ["Delhi is the capital of India.", 
"Langchain is a framework for developing applications powered by language models."]

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
result = embedding.embed_documents("documents")
print(str(result))