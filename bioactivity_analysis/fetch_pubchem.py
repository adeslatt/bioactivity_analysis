import requests

def fetch_pubchem_bioactivity(uniprot_id):
    """
    Fetch bioactivity data from PubChem for a given UniProt ID.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/ProteinGI/UniProtID/{uniprot_id}/concise/JSON"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('Table', {}).get('Row', [])
    return []
