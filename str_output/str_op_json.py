from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# This is a plain JSON Schema
# It is just a Python dict, not a class, not Pydantic, not TypedDict

json_schema = {
  # Title is just a label for the schema
  "title": "Review",

  # This tells: output must be a JSON object
  "type": "object",

  # All fields that the LLM should return
  "properties": {

    # key_themes must be an array of strings
    # No runtime validation, only guides the LLM
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },

    # summary must be a string
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },

    # sentiment must be a string and only one of these values
    # This is only a rule for the LLM, not strict runtime validation
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },

    # pros can be either an array of strings OR null
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },

    # cons can be either an array of strings OR null
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },

    # name can be either a string OR null
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },

  # These fields MUST be present in the output
  # If missing, LangChain may retry or fail
  "required": ["key_themes", "summary", "sentiment"]
}


# with_structured_output reads this JSON schema
# It tells the LLM to return JSON in exactly this structure
# But it does NOT do strong runtime validation like Pydantic
structured_model = model.with_structured_output(json_schema)


# The result is just a normal dict
# No automatic type checking or coercion happens
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
print(result)