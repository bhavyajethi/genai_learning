from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# This HF endpoint is used to access a particular model hosted on Hugging Face with the specified task.
llm = HuggingFaceEndpoint(
    repo_id = "tiiuae/Falcon-H1R-7B",
    task = "text-generation",
    provider="hf-inference",
    hf_access_token = load_dotenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of india")
print(result.content)