from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal

load_dotenv()
model = ChatGoogleGenerativeAI()
class Review(TypedDict):
    themes: Annotated[list[str], "List all the key themes discusses in the review in a list"]
    summary: Annotated[str, "Write a summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return a sentiment of the review from either positive or negative"]
    pros: Annotated[Optional[list[str]], "List all the pros of the review in a list"]
    cons: Annotated[Optional[list[str]], "List all the cons of the review in a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer of the summary"]

    