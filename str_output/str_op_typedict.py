from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# TypedDict is only a TYPE HINT, not a real runtime object
# It does NOT validate anything at runtime

class Review(TypedDict):

    # Annotated is used to attach extra metadata (description)
    # Because TypedDict has no Field(...) like Pydantic
    # LangChain reads this text to guide the LLM
    themes: Annotated[list[str], "List all the key themes discusses in the review in a list"]

    # No runtime validation here, just a hint for structure
    summary: Annotated[str, "Write a summary of the review"]

    # Literal here is only for typing + prompt guidance
    # If LLM returns something else, no error will happen
    sentiment: Annotated[Literal["pos", "neg"], "Return a sentiment of the review from either positive or negative"]

    # Optional means key can be missing or None
    # But no runtime check is done
    pros: Annotated[Optional[list[str]], "List all the pros of the review in a list"]

    # Same here, no validation
    cons: Annotated[Optional[list[str]], "List all the cons of the review in a list"]

    # Just a typing hint + description
    name: Annotated[Optional[str], "Write the name of the reviewer of the summary"]

# with_structured_output reads the TypedDict fields + Annotated text
# It only guides the LLM, it does NOT validate the result
structured_model = model.with_structured_output(Review)

# The result is just a normal dict
# Wrong types or wrong values will NOT cause an error
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Bhavya Jethi
""")

# Access like a normal dict
print(result['name'])