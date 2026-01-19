from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
    # When we pass a list of tuples like ('system', '...') to ChatPromptTemplate, LangChain looks at the first element (the "key") of each tuple. LangChain has a "lookup dictionary" that maps these strings to the message classes we used earlier (SystemMessage, etc.). This is known as Schema Mapping. 
    [
        ('system', 'You are a helpful AI bot. Your name is {name}'),
        ('human', 'hello how are you doing'),
        ('ai', 'I am doing well, thanks!'),
        ('human', '{user_input}'),
    ]
)

# In Python, this is called a trailing comma. It is technically optional in a list, but it is considered "Best Practice" because:
# Cleaner Diffs: If a new message is added later, the version control (like Git) only shows 1 new line added instead of 1 line modified (to add the comma) plus 1 line added.
# Ease of Reordering: Lines can be moved up and down without breaking the code because every line already has a comma.

prompt_value = template.invoke(
    {
    'name': 'Bob',
    'user_input': 'What is your name',
    }
)