from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0)
template = PromptTemplate.from_template(
    """Extract the following from this clinical note:
- Age
- Gender
- Symptoms
- Diagnoses
Return as a JSON.

Note:
{note}
""")

def extract_patient_info(note):
    chain = template | llm
    return chain.invoke({"note": note})
