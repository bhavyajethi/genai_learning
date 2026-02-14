from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('doc_loaders\dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    # The separator in CharacterTextSplitter is a crucial parameter that defines the specific character or string used as a breakpoint for dividing the text into smaller, manageable chunks. 
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)