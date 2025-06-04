import requests

def search_pubmed(query):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10}
    r = requests.get(url, params=params)
    return r.json()["esearchresult"]["idlist"]

def fetch_pubmed_abstracts(pmid_list):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "retmode": "text", "rettype": "abstract", "id": ",".join(pmid_list)}
    r = requests.get(url, params=params)
    return r.text
