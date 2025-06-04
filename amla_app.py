import streamlit as st
from agents.intake_agent import extract_patient_info
from agents.query_agent import generate_search_queries
from api_clients.pubmed import search_pubmed, fetch_pubmed_abstracts
from agents.summarizer import summarize_documents
from utils.state_manager import save_state, load_state

st.set_page_config(page_title="AMLA-PES", layout="wide")
st.title("🧠 AMLA-PES: Personalized Medical Literature Summarizer")

note = st.text_area("Paste EHR Note or Patient Intake Form")

if st.button("Generate Summary"):
    with st.spinner("🔍 Extracting patient info..."):
        patient_info = extract_patient_info(note)
        st.json(patient_info)

    with st.spinner("🔎 Generating PubMed query..."):
        query = generate_search_queries(patient_info)
        st.write("**Generated Query:**", query)

    with st.spinner("📚 Fetching PubMed abstracts..."):
        pmids = search_pubmed(query)
        abstracts = fetch_pubmed_abstracts(pmids)
        st.write("**Retrieved Abstracts:**", len(abstracts))

    with st.spinner("📝 Summarizing and formatting LaTeX report..."):
        summary = summarize_documents(abstracts, patient_info)
        st.markdown(summary)

    save_state({"note": note, "query": query, "pmids": pmids})
