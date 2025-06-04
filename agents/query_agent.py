rom langchain.prompts import PromptTemplate

query_template = PromptTemplate.from_template(
    """Given this extracted patient info:
{info}

Generate a concise PubMed search query string:
""")

def generate_search_queries(info):
    return (query_template | ChatOpenAI(temperature=0)).invoke({"info": info})

