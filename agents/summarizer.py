from langchain.prompts import PromptTemplate

def summarize_documents(abstracts, patient_info):
    summary_prompt = PromptTemplate.from_template(
        """Use the following abstracts:
{abstracts}

And this patient info:
{info}

Summarize the relevant findings and format as a LaTeX medical report:
""")
    return (summary_prompt | ChatOpenAI(temperature=0.3)).invoke({
        "abstracts": abstracts,
        "info": patient_info
    })
