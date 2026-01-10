from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache' # Set the Hugging Face cache directory

# this HF pipeline is used to access and download a particular model from HF in our local machine.
llm = HuggingFacePipeline.from_model_id(
    model_id='tiiuae/Falcon-H1R-7B',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)