from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# We use BaseModel from Pydantic
# This creates a real runtime object, not just a type hint
class Review(BaseModel):
    # Pydantic reads this type and will VALIDATE it at runtime
    # If LLM returns something else, it will throw an error
    themes: list[str] = Field(description = "List all the key themes discusses in the review in a list")

    # Normal string field, must be a string or it fails
    summary: str = Field(description = "Write a summary of the review")

    # Literal means only "pos" or "neg" are allowed
    # If model returns anything else, validation error comes
    sentiment: Literal["pos", "neg"] = Field(description = "Return a sentiment of the review from either positive or negative")

    # Optional means it can be missing or None
    # Pydantic still checks if it's a list of strings if present
    pros: Optional[list[str]] = Field(description="List all the pros of the review in a list")

    # Same as above, validated at runtime
    cons: Optional[list[str]] = Field(description ="List all the cons of the review in a list")

    # Optional string, runtime validation happens
    name: Optional[str] = Field(description = "Write the name of the reviewer of the summary")


# .with_structured_output, Langchain basically extracts the text from the schema Review, turns that into a prompt + op_parser and coerces it with the response of the model.
structured_model = model.with_structured_output(Review)

# The result is a Pydantic object, not a dict
# You can access fields like: result.name
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


# If the LLM returns wrong types or missing required fields,
# Pydantic will throw an error here
print(result)